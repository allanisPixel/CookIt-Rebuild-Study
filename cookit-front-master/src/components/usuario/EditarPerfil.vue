<template>
  <div class="container" v-bind:key="user.id">
    <div class="row py-5 mt-5 align-items-center">
      <!-- Registeration Form -->
      <div class="align-content col-md-7 mt-3">
        <form @submit.prevent="setPerfil">
          <div class="row">
            <!-- Usuário -->
            <div class="input-group col-lg-12 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-user text-muted"></i>
                </span>
              </div>
              <input
                id="username"
                type="text"
                name="username"
                placeholder="Usuário"
                class="form-control bg-white border-left-0 border-md"
                v-model="user.username"
              />
            </div>
            <!-- Primeiro nome -->
            <div class="input-group col-lg-6 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-user text-muted"></i>
                </span>
              </div>
              <input
                id="firstName"
                type="text"
                name="first_name"
                placeholder="Nome"
                class="form-control bg-white border-left-0 border-md"
                v-model="user.first_name"
              />
            </div>

            <!-- Último nome -->
            <div class="input-group col-lg-6 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-user text-muted"></i>
                </span>
              </div>
              <input
                id="lastName"
                type="text"
                name="last_name"
                placeholder="Sobrenome"
                class="form-control bg-white border-left-0 border-md"
                v-model="user.last_name"
              />
            </div>

            <!-- Endereço de email -->
            <div class="input-group col-lg-12 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-envelope text-muted"></i>
                </span>
              </div>
              <input
                id="email"
                type="email"
                name="email"
                placeholder="Email"
                class="form-control bg-white border-left-0 border-md"
                v-model="user.email"
              />
            </div>

            <!-- Senha -->
            <div class="input-group col-lg-6 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-lock text-muted"></i>
                </span>
              </div>
              <input
                id="password"
                type="password"
                name="password"
                placeholder="Senha"
                class="form-control bg-white border-left-0 border-md"
                v-model="current_password"
              />
            </div>

            <!-- Confirmação de senha -->
            <div class="input-group col-lg-6 mb-4">
              <div class="input-group-prepend">
                <span
                  class="
                    input-group-text
                    bg-white
                    px-4
                    border-md border-right-0
                  "
                >
                  <i class="fa fa-lock text-muted"></i>
                </span>
              </div>
              <input
                id="passwordConfirmation"
                type="password"
                name="re_password"
                placeholder="Confirme sua senha"
                class="form-control bg-white border-left-0 border-md"
                v-model="user.re_password"
              />
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              class="btn btn-primary mx-auto"
              @click="setPerfil()"
              style="width: 95%"
            >
              Alterar dados
            </button>
            <!-- Divider Text -->
            <div
              class="
                form-group
                col-lg-12
                mx-auto
                d-flex
                align-items-center
                my-4
              "
            >
              <div class="border-bottom w-100 ml-5"></div>

              <div class="border-bottom w-100 mr-5"></div>
            </div>
            <!---
            <input
              id="firstName"
              type="password"
              name="username"
              placeholder="Usuário"
              class="form-control bg-white border-left-0 border-md"
              v-model="current_password"
            />

            <button
              name="delete"
              class="btn btn-primary mx-auto"
              @click="deletePerfil()"
              style="width: 95%"
            >
              Deletar conta
            </button>
            --->


            <button
              name="deactivation"
              class="btn btn-primary mx-auto"
              @click="desativarConta()"
              style="width: 95%"
            >
              Desativar conta
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "EditarPerfil",
  components: {},

  data() {
    return {
      current_password: "",
      user: "",
      is_active: "",
    };
  },

  mounted() {
    this.getPerfil();
  },

  methods: {
    getPerfil() {
      axios
        .get("/api/users/me")
        .then((response) => (this.user = response.data));
    },

    setPerfil() {
      axios
        .put("/api/users/me/", this.user)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async deletePerfil() {
      await axios
        .delete("/api/users/me/", {
          data: {
            current_password: this.current_password,
          },
        })
        .then((response) => {
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token");
          this.$store.commit("removeToken");
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

    async desativarConta() {
      this.getPerfil();
      this.user.visivel = false;
      this.setPerfil();
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>


<style scoped>
body {
  min-height: 50vh;
}



button{
  background-color: #f2780c;
  border-color: #f2780c;
}

.form-control:not(select) {
  padding: 1.5rem 0.5rem;
  border-color: #f2b950
}

select.form-control {
  height: 52px;
  padding-left: 0.5rem;
}

.form-control::placeholder {
  color: #ccc;
  font-weight: bold;
  font-size: 0.9rem;
}
.form-control:focus {
  box-shadow: none;
}

.align-content {
  margin: auto;
  width: 60%;
  padding: 10px;
}

</style>