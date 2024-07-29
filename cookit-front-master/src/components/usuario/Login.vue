<template>
  <v-container>
    <h1>Entre na sua Conta.</h1>
    <v-form @submit.prevent="submitForm">
      <v-text-field
        rounded
        outlined
        v-model="username"
        :type="'email'"
        label="E-mail"
        required
        name="email"
      ></v-text-field>

      <v-text-field
        rounded
        outlined
        v-model="password"
        :type="'password'"
        label="Senha"
        name="password"
      ></v-text-field>

      <v-btn
        color="#F2780C"
        large
        block
        rounded
        class="mr-4"
        type="submit"
        name="submit_form"
      >
        LOGIN
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",
  data() {
    return {
      user: "",
      username: "",
      password: "",
      errors: [],
    };
  },

  methods: {
    async reativarConta() {
      axios.get("/api/users/me").then((response) => {
        this.user = response.data;

        if (!this.user.visivel) {
          this.user.visivel = true;
          axios.put("/api/users/me/", this.user).catch((error) => {
            console.log(error);
          });
        }
      });
    },

    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        password: this.password,
        email: this.username,
      };

      await axios
        .post("/api/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          console.log(response.data);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          this.$router.push("/");
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            console.log(JSON.stringify(error.message));
          } else {
            console.log(JSON.stringify(error));
          }
        });
      await axios
        .get("/api/users/me/")
        .then((response) => {
          this.$store.commit("setUser", response.data);
          localStorage.setItem("user", response.data);
        })
        .catch((error) => console.log(error));
      this.reativarConta();
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  font-family: Montserrat;
  font-weight: bolder;
}
</style>