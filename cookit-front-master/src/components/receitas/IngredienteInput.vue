<template>
  <v-sheet class="pa-3 mb-10" outlined color="var(--color1">
    <v-input>
      <v-text-field
        outlined
        rounded
        class="rounded-r-0"
        hide-details
        v-model="nomeIngrediente"
        background-color="white"
      ></v-text-field>
      <v-btn
        dark
        @click="addTag"
        color="var(--color2)"
        rounded
        class="rounded-l-0"
        x-large
      >
        <v-icon>fas fa-plus</v-icon>
      </v-btn>
    </v-input>
    <v-row>
      <v-col
        v-for="(ing, index) in ingredientes"
        :key="'ingrediente' + index"
        md="6"
        sm="12"
      >
        <v-chip dark class="ma-2" close @click:close="removeTag(index)">
          <v-text-field
            color="none"
            dense
            hide-details
            v-model="ing.nome_ingrediente"
            name="nome_ingrediente"
          >
          </v-text-field>
          <v-text-field
            type="number"
            dense
            hide-details
            v-model="ing.quantidade_ingrediente"
            name="quantidade_ingrediente"
          >
          </v-text-field>
          <v-select
            dense
            hide-details
            :items="ingredienteUnidadeData"
            item-text="text"
            item-value="char"
            v-model="ing.unidade_medida_ingrediente"
            name="unidade_medida_ingrediente"
          ></v-select>
        </v-chip>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import axios from "axios";

export default {
  name: "IngredienteInput",

  props: ["ingredientes"],

  data() {
    return {
      ingrediente_ids: [],
      ing_ativo: null,
      nomeIngrediente: "",
      ingredienteUnidadeData: [
        {
          char: "U",
          text: "Unidade",
        },
        {
          char: "X",
          text: "Xícara",
        },
        {
          char: "C",
          text: "Colher de Sopa",
        },
        {
          char: "CH",
          text: "Colher de Chá",
        },
        {
          char: "M",
          text: "Mililitro(ml)",
        },
        {
          char: "L",
          text: "Litros",
        },
        {
          char: "G",
          text: "Gramas(g)",
        },
        {
          char: "KG",
          text: "Quilograma(kg)",
        },
        {
          char: "AGS",
          text: "a gosto",
        },
      ],
    };
  },
  methods: {
    addIngredientes() {
      for (var i = 0; i < this.ingredientes.length; i++) {
        axios({
          method: "post",
          url: "/api/ingrediente/",
          data: this.ingredientes[i],
          auth: {
            username: "admin",
            password: "12345",
          },
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            // your action after success
            // this.ingrediente_ids.push(response.id)
            this.ingrediente_ids.push(response.data.id);
            console.log(response);
          })
          .catch((error) => {
            // your action on error success
            console.log(error);
          });
      }
      console.log(this.ingredientes);
    },
    addTag() {
      if (this.nomeIngrediente != "") {
        console.log(this.ingrediente);
        var ing = {
          nome_ingrediente: this.nomeIngrediente,
          quantidade_ingrediente: 1,
          unidade_medida_ingrediente: "U",
        };
        this.ingredientes.push(ing);
        this.nomeIngrediente = "";
      }
    },
    removeTag(index) {
      this.ingredientes.splice(index, 1);
    },
    getIngredientes() {
      return this.ingredientes;
    },
  },
};
</script>

<style scoped>
.v-text-field > .v-input__control > .v-input__slot:before {
    border-style: none;
}
</style>