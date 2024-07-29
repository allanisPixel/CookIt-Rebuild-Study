<template>
  <v-card class="image-input mb-10">
    <v-img
      height="100%"
      class="align-end"
      v-if="url != null"
      rounded
      v-bind:src="url"
    >
      <v-card-title>
        <v-file-input
          class="ms-3 me-3"
          width="100%"
          v-model="foto"
          accept="image/png, image/jpeg, image/bmp"
          prepend-icon="mdi-camera"
          @change="onFileChange"
          hide-details
          dark
        >
        </v-file-input>
      </v-card-title>
    </v-img>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  name: "ImageInput",

  data() {
    return {
      foto: null,
      url: "",
    };
  },

  methods: {
    onFileChange() {
      //const file = e.target.files[0];
      if (this.foto != null) {
        this.url = URL.createObjectURL(this.foto);
      } else {
        this.url = "";
      }
      this.$emit("mudarFoto", this.foto);
    },
    uploadPhoto() {
      axios
        .put(
          "/upload/",
          { file: this.foto },
          {
            headers: {
              "Content-Disposition": "attachment; filename = this.foto.name",
            },
          }
        )
        .then((response) => {
          axios.defaults.headers.common["Access-Control-Allow-Headers"] = "*";
          axios.defaults.headers.common["Access-Control-Allow-Methods"] =
            "GET, POST, PUT, DELETE, OPTIONS";
          console.log(axios.defaults.headers);
          console.log(response.headers);
        })
        .catch((error) => console.log(error.response.data));
    },
  },
};
</script>

<style>
.image-input {
  width: 100%;
  height: 200px;
  background-color: var(--color1) !important;
}
.image-input .v-file-input button {
  background-color: var(--color2);
  padding: 0.5em;
  border-radius: 1em;
  margin: 0;
}
.image-input .v-text-field__slot {
  display: none !important;
}
.image-input .v-input__slot::before {
  border-style: none !important;
}
</style>