<template>
  <div v-bind:key="user.id" class="container">
    <div id="receita-receita-completa">
      <div id="dados-receita-completa">
        <div class="row" id="nome-junto-da-foto">
          <div id="thumbnails-receita-completa">
            <div class="row">
              <!--TODO: ver uma formatação melhor para a imagem-->
              <img
                class="receita-foto rounded-circle"
                style="max-width: 800px"
                v-bind:src="user.foto_usuario"
                alt=""
              />
            </div>
          </div>

          <div id="titulo-receita-completa" class="col">
            <h3>{{ user.first_name }} {{ user.last_name }}</h3>
            <v-rating
              :value="4.5"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
            ></v-rating>
          </div>
        </div>

        <v-card>
          <v-tabs color="orange accent-4" right id="modificar-card-trasicao">
            <v-tab>Receitas</v-tab>
            <v-tab>favoritos</v-tab>

            <v-tab-item>
              <v-card flat>
                <v-row class="pl-6 pr-6">
                  <v-col
                    md="4"
                    sm="12"
                    v-for="receita in receitas"
                    :key="receita.id"
                  >
                    <resumo-receita :receita="receita" />
                  </v-col>
                </v-row>
              </v-card>
            </v-tab-item>

            <v-tab-item>
              <v-card flat>
                <p>Null</p>
              </v-card>
            </v-tab-item>
          </v-tabs> </v-card
        ><!--Final do v-card-->
      </div>
      <!--Final do if-->
    </div>
    <!--Final: div id="receita completa"-->
  </div>
  <!--Final: v-bind:key="user.id" class="container"-->
</template>

<script>
import axios from "axios";
import ResumoReceita from "../parciais/ResumoReceita";

// import Sidebar from "./parciais/Sidebar";
//import { mapActions } from "vuex";

export default {
  name: "Index",
  data() {
    return {
      user: "",
      receitas: [],
    };
  },

  components: {
    ResumoReceita,
  },

  mounted() {
    this.getUser();
  },

  methods: {
    getUser() {
      axios
        .get("/api/user/" + this.$route.params.id)
        .then((response) => {
          this.user = response.data;
          return axios.get(
            "/api/usuario-receita/?dono_receita__in=" + this.user.id
          );
        })
        .then((response) => (this.receitas = response.data));
    },
  },
};
</script>

<style scoped>
.container {
  margin: 0 auto;
  margin-top: 80px;
  border-left: 1px;
  border-right: 1px;
}

/*impor*/
#receita-receita-completa {
  border: 1px solid white;
  border-radius: 1em;
  /*background-color: orange;*/
}
#dados-receita-completa {
  background-color: #f5fffa;
  border: 1px;
  border-radius: 1em;
  margin: 1em;
  padding: 1em;
}

#titulo-receita-completa {
  text-align: left;
  padding: 78px;
}

#titulo-receita-completa h3 {
  color: #aba11b;
}

#usuario-receita-completa i {
  font-size: 4em;
}

.receita-foto {
  object-fit: cover;
  /* Do not scale the image */
  object-position: center;
  /* Center the image within the element */
  width: 120px;
  height: 120px;
  margin: 60px;
  margin-bottom: 1rem;
  border: 1px solid #707070;
}

#nome-junto-da-foto {
  column-width: 10em;
  column-rule: 1px solid rgb(75, 70, 74);
}

#modificar-card-trasicao {
  border-radius: 100px;
}
</style>