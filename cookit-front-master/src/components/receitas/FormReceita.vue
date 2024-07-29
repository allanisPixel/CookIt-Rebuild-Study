<template>
  <v-container class="mt-5 mb-5">
    <v-form @submit.prevent="addReceita">
      <v-text-field
        v-model="nome_receita"
        label="Nome da Receita"
        rounded
        outlined
        name="nome_receita"
      >
      </v-text-field>
      <image-input @mudarFoto="fotos = $event" />
      <v-select
        v-model="categoria"
        name="categoria"
        :items="$store.state.receitas.categoriareceita"
        item-text="valor"
        item-value="letra"
        label="Categoria"
        rounded
        outlined
      >
      </v-select>
      <v-row class="mb-0 mt-0">
        <v-col class="pb-0 pt-0" md="6" sm="12">
          <v-select
            v-model="sabor_receita"
            :items="$store.state.receitas.saborreceita"
            item-text="valor"
            item-value="letra"
            label="Sabor"
            rounded
            outlined
            name="sabor_receita"
          />
        </v-col>
        <v-col class="pb-0 pt-0" md="6" sm="12">
          <v-select
            v-model="dificuldade"
            name="dificuldade"
            :items="$store.state.receitas.dificuldadereceita"
            item-text="valor"
            item-value="letra"
            label="Dificuldade"
            rounded
            outlined
          />
        </v-col>
      </v-row>
      <v-row class="mb-0 mt-0">
        <v-col class="pb-0 pt-0" md="6" sm="12">
          <v-text-field
            v-model="porcoes"
            label="Porções"
            type="number"
            rounded
            outlined
            name="porcoes"
          />
        </v-col>
        <v-col class="pb-0 pt-0" md="6" sm="12">
          <v-label>Tempo de Preparo</v-label>
          <v-input>
            <v-text-field
              v-model="tempo_preparo"
              dense
              type="number"
              name="tempo_preparo"
            >
            </v-text-field>
            <v-select
              v-model="tempo_unidade_medida"
              :items="$store.state.receitas.tempopreparo"
              item-text="valor"
              item-value="letra"
              dense
              name="tempo_unidade_medida"
            ></v-select>
          </v-input>
        </v-col>
      </v-row>

      <ingrediente-input v-bind:ingredientes="ingredientes" />
      <v-textarea
        outlined
        no-resize
        label="Modo de Preparo"
        v-model="modo_preparo"
        name="modo_preparo"
      ></v-textarea>

      <v-textarea
        outlined
        no-resize
        label="Observações Adicionais"
        v-model="observacoes_adicionais"
        name="observacoes_adicionais"
      ></v-textarea>
      <v-btn
        name="submit-button"
        type="submit"
        dark
        color="var(--color2)"
        x-large
        block
        class="rounded-pill"
        ><strong>PUBLICAR RECEITA</strong></v-btn
      >
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
import IngredienteInput from "./IngredienteInput";
import ImageInput from "../parciais/ImageInput";

export default {
  name: "FormReceita",

  components: {
    IngredienteInput,
    ImageInput,
  },

  data() {
    return {
      categoria2: [
        {
          value: "C",
          name: "Café da manhã",
        },
        {
          value: "A",
          name: "Almoço",
        },
        {
          value: "L",
          name: "Lanche",
        },
        {
          value: "J",
          name: "Janta",
        },
        {
          value: "S",
          name: "Sobremesas",
        },
        {
          value: "B",
          name: "Bebidas",
        },
        {
          value: "V",
          name: "Vegana",
        },
      ],

      nome_receita: "",
      modo_preparo: "",
      porcoes: 0,
      sabor_receita: "D",
      tempo_preparo: 0,
      tempo_unidade_medida: "M",
      fotos: null,
      categoria: "A",
      dificuldade: "F",
      data_publicacao: "",
      slug: "",
      observacoes_adicionais: "",
      ingredientes: [],
      dono_receita: "",
      //Tag Ingrediente
    };
  },

  methods: {
    addReceita() {
      axios({
        method: "post",
        url: "/api/post-receita/",
        data: {
          nome_receita: this.nome_receita,
          modo_preparo: this.modo_preparo,
          dono_receita: this.$store.state.auth.user.id,
          porcoes: this.porcoes,
          sabor_receita: this.sabor_receita,
          tempo_preparo: this.tempo_preparo,
          tempo_unidade_medida: this.tempo_unidade_medida,
          //fotos: this.fotos,
          fotos: null,
          categoria: this.categoria,
          dificuldade: this.dificuldade,
          data_publicacao: this.data_publicacao,
          slug: this.slug,
          observacoes_adicionais: this.observacoes_adicionais,
          ingredientes: this.ingredientes,
        },
      })
        .then((response) => {
          this.nome_receita = "";
          this.modo_preparo = "";
          this.porcoes = 0;
          this.sabor_receita = "";
          this.tempo_preparo = 0;
          this.tempo_unidade_medida = "";
          this.fotos = null;
          this.categoria = "";
          this.dificuldade = "";
          this.data_publicacao = "";
          this.slug = "";
          this.observacoes_adicionais = "";
          this.ingredientes = [];

          console.log(response);
          this.$router.push({
            name: "PaginaReceita",
            params: { id: response.data.id },
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.container { background-color: white; }
</style>