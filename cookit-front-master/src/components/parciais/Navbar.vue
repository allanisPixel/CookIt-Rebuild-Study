<template>
  <v-app-bar app light clipped-left>
    <router-link to="/">
      <v-img
        class="brand"
        alt="CookIt Logo"
        contain
        src="@/assets/cookit_logo.svg"
        transition="scale-transition"
        width="100"
      />
    </router-link>

    <v-spacer></v-spacer>

    <div class="d-flex">
      <v-text-field
        outlined
        placeholder="Pesquise sua Receita..."
        single-line
        background-color="white"
        dense
        hide-details
        class="rounded-l-xl rounded-r-0"
        size="default"
        v-model="$store.state.receitas.pesquisa.nome_receita"
        width="200px"
        name="search-input"
      ></v-text-field>
      <v-btn
        dark
        class="rounded-r-xl rounded-l-0"
        height="40px"
        @click="$store.dispatch('basicSearch')"
        name="search-button"
      >
        <v-icon>fas fa-search</v-icon>
      </v-btn>
    </div>

    <v-spacer></v-spacer>
    <v-spacer></v-spacer>

    <div v-if="$store.state.auth.isAuthenticated">
      <v-btn icon dark @click="$router.push('FormReceita')">
        <v-icon>fas fa-book</v-icon>
      </v-btn>
      <v-btn icon dark>
        <v-icon>fas fa-bell</v-icon>
      </v-btn>
      <v-menu>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon dark v-bind="attrs" v-on="on">
            <v-icon>$cookit_user</v-icon>
          </v-btn>
        </template>
        <v-card class="">
          <v-list class="pa-0">
            <v-list-item class="pa-0">
              <v-card-title class="bg">
                <v-avatar size="56">
                  <v-icon>$cookit_user_circle</v-icon>
                </v-avatar>
                <v-btn
                  text
                  class="ml-3"
                  @click="
                    $router.push({
                      name: 'Perfil',
                      params: { id: $store.state.auth.user.id },
                    })
                  "
                >
                  {{ $store.state.auth.user.first_name }}
                  {{ $store.state.auth.user.last_name }}</v-btn
                >
              </v-card-title>
            </v-list-item>
            <v-list-item>
              <v-card-actions>
                <v-btn text to="/FormReceita">Publicar Receita</v-btn>
              </v-card-actions>
            </v-list-item>
            <v-list-item>
              <v-card-actions>
                <v-btn text to="EditarPerfil">Editar Perfil</v-btn>
              </v-card-actions>
            </v-list-item>
            <v-list-item>
              <v-card-actions>
                <v-btn text @click="logout()">Logout</v-btn>
              </v-card-actions>
            </v-list-item>
          </v-list>
        </v-card>
      </v-menu>
    </div>

    <div v-else>
      <v-btn to="/Login">Login</v-btn>
      <v-btn to="/Cadastro">Cadastro</v-btn>
    </div>
  </v-app-bar>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "Navbar",
  computed: mapGetters(["getPesquisa"]),

  data() {
    return {
      search_term: "",
    };
  },

  methods: {
    ...mapActions(["basicSearch"]),
    logout() {
      axios
        .post("/api/token/logout/")
        .then((response) => {
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token");
          localStorage.removeItem("user");
          this.$store.commit("removeToken");
          this.$store.commit("removeUser");
          this.$router.push("/");
          return response;
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            console.log(JSON.stringify(error.message));
          } else {
            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>

<style scoped>
.user-card {
  position: fixed;
}
.bg {
  background-color: var(--color4) !important;
}
.brand {
  filter: invert(100%);
}
</style>
