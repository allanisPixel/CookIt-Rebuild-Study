<template>
  <v-container v-bind:key="receita.id" class="mt-5 mb-5">
    <v-form @submit.prevent="setReceita">
      <v-text-field
        v-model="receita.nome_receita"
        label="Nome da Receita"
        rounded
        outlined
        name="nome_receita"
      >
      </v-text-field>
      <image-input @mudarFoto="fotos = $event" />
      <v-select
        v-model="receita.categoria"
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
            v-model="receita.sabor_receita"
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
            v-model="receita.dificuldade"
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
            v-model="receita.porcoes"
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
              v-model="receita.tempo_preparo"
              dense
              type="number"
              name="tempo_preparo"
            >
            </v-text-field>
            <v-select
              v-model="receita.tempo_unidade_medida"
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
        v-model="receita.modo_preparo"
        name="modo_preparo"
      ></v-textarea>

      <v-textarea
        outlined
        no-resize
        label="Observações Adicionais"
        v-model="receita.observacoes_adicionais"
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
        ><strong>PUBLICAR RECEITA</strong>
       </v-btn>
       <br>
       <v-btn
        id="submit-button"
        @click="deleteReceita(receita.id)"
        class="btn btn-primary btn-block rounded-pill"
        name="submit-button"
        dark
        color="var(--color2)"
        x-large
        block
        ><strong>EXCLUIR RECEITA</strong>
       </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
import IngredienteInput from "./IngredienteInput";
import ImageInput from "../parciais/ImageInput";
import { mapActions } from "vuex";

export default {
  name: "FormReceita",

  components: {
    IngredienteInput,
    ImageInput,
  },

  data() {
    return {
      receita: "",
      ingredientes: [],
    };
  },

    mounted(){ 
        this.getReceita(); 
    },
  
  methods: {
    getReceita() {
      axios
        .get("/api/post-receita/" + this.$route.params.id)
        .then(
          (response) => (
            (this.receita = response.data),
            (this.ingredientes = response.data.ingredientes)
          )
        );
    },

    ...mapActions(["deleteReceita"]),

    setReceita() {
      this.receita.ingredientes = this.ingredientes;
      axios
        .put("/api/post-receita/" + this.$route.params.id + "/", this.receita)
        .then((response) => {
          this.$router.push({
            name: "PaginaReceita",
            params: { id: response.data.id },
          });
          console.log(response);
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