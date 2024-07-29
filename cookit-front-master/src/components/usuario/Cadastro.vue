<template>
  <v-container>
    <h1>Bem Vindo ao CookIt!</h1>
    <v-form @submit.prevent="submitForm">
      <v-row>
        <v-col>
          <v-text-field
            rounded
            outlined
            v-model="first_name"
            label="Nome"
            required
            name="first_name"
          ></v-text-field>
        </v-col>

        <v-col>
          <v-text-field
            rounded
            outlined
            v-model="last_name"
            label="Sobrenome"
            required
            name="last_name"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-text-field
        rounded
        outlined
        v-model="username"
        label="Usuario"
        required
        name="username"
      ></v-text-field>

      <v-text-field
        rounded
        outlined
        v-model="email"
        :type="'email'"
        label="E-mail"
        required
        name="email"
      ></v-text-field>

      <v-row>
        <v-col>
          <v-text-field
            rounded
            outlined
            v-model="password"
            :type="'password'"
            label="Senha"
            name="password"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            rounded
            outlined
            v-model="re_password"
            :type="'password'"
            label="Repita a Senha"
            required
            name="re_password"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-btn
        color="#F2780C"
        large
        block
        rounded
        class="mr-4"
        type="submit"
        name="submit_form"
      >
        CRIAR CONTA
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Cadastro",
  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      password: "",
      email: "",
      re_password: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        first_name: this.first_name,
        last_name: this.last_name,
        password: this.password,
        email: this.email,
        re_password: this.re_password,
      };

      axios
        .post("/api/users/", formData)
        .then((response) => {
          console.log(response);
          this.$router.push("/login");
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