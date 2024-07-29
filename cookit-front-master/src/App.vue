<template>
  <v-app>
    <navbar />

    <v-main>
      <router-view />
    </v-main>
    <v-footer color="var(--color3)" padless>
      <v-row justify="center" no-gutters>
        <v-col class="py-4 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} — <strong>Cookit</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import Navbar from "@/components/parciais/Navbar";
import axios from "axios";

export default {
  name: "App",

  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.auth.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
      axios.get("/api/users/me").then((response) => {
        this.$store.state.auth.user = response.data;
      });
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },

  components: {
    Navbar,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: Montserrat, Verdana, Geneva, Tahoma, sans-serif;
  border: none;
}

:root {
  --color1: #f2b950;
  --color2: #f2780c;
  --color3: #f24822;
  --color4: #f2f2f2;
  --color5: #2d2d2d;
}
.v-app-bar {
  background-color: var(--color3) !important;
} /*
.v-card,
.v-text-field:not(.classificar-por) {
  border: 2px solid var(--color4) !important;
}*/
.v-btn {
  box-shadow: none !important;
}
a {
  text-decoration: none;
  color: inherit !important;
}
.v-chip {
  background-color: var(--color2) !important;
}
.v-main {
  background-color: var(--color4);
}
.v-footer {
  z-index: 10;
}
</style>
