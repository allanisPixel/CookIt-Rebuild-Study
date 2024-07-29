<template>
  <div>
    <sidebar />
    <v-row class="ma-0">
      <v-col class="" sm="12" md="6">
        <div class="d-flex">
          <v-text-field
            class="rounded-l-xl rounded-r-0"
            dense
            outlined
            background-color="white"
            hide-details
            v-model="tenha_nome"
            placeholder="Quero que tenha..."
          >
          </v-text-field>
          <v-btn
            class="rounded-r-xl rounded-l-0"
            large
            color="success"
            @click="addTag(tenha, tenha_nome)"
          >
            <v-icon>fas fa-plus</v-icon>
          </v-btn>
        </div>
        <div v-for="i in tenha" :key="i">
          <v-chip dark class="ma-2" close @click:close="removeTag(tenha, i)">
            {{ i }}
          </v-chip>
        </div>
      </v-col>
      <v-col class="">
        <div class="d-flex">
          <v-text-field
            class="rounded-l-xl rounded-r-0"
            dense
            outlined
            background-color="white"
            hide-details
            v-model="naotenha_nome"
            placeholder="Quero que não tenha..."
          >
          </v-text-field>
          <v-btn
            class="rounded-r-xl rounded-l-0"
            large
            color="error"
            @click="addTag(naotenha, naotenha_nome)"
          >
            <v-icon>fas fa-plus</v-icon>
          </v-btn>
        </div>
        <div v-for="i in naotenha" :key="i">
          <v-chip class="ma-2" close @click:close="removeTag(naotenha, i)">
            {{ i }}
          </v-chip>
        </div>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0">
      <v-col>
        <v-btn
          class="hidden-lg-and-up"
          icon
          @click.stop="$store.state.drawer = !$store.state.drawer"
        >
          <v-icon>fas fa-bars</v-icon>
        </v-btn>
      </v-col>
      <v-col class="pa-0 ma-0"></v-col>
      <v-col class="pa-0 ma-0" cols="3">
        <v-select
          class="classificar-por"
          hide-details
          dense
          label="Classificar por"
          :items="order"
        >
        </v-select>
      </v-col>
    </v-row>
    <v-row class="pl-6 pr-6">
      <v-col
        md="4"
        sm="12"
        v-for="receita in $store.state.receitas.receitas"
        :key="receita.id"
      >
        <resumo-receita :receita="receita" />
      </v-col>
    </v-row>
    <!--<v-pagination :length="6" class="my-5"></v-pagination>-->
  </div>
</template>

<script>
import Sidebar from "./parciais/Sidebar";
import ResumoReceita from "./parciais/ResumoReceita.vue";

export default {
  name: "Index",

  data() {
    return {
      tenha: this.$store.state.receitas.pesquisa.ingredientes,
      naotenha: this.$store.state.receitas.pesquisa.n_ingredientes,
      tenha_nome: "",
      naotenha_nome: "",
    };
  },

  components: {
    Sidebar,
    ResumoReceita,
  },

  methods: {
    addTag(tags, nome) {
      if (nome != "") {
        tags.push(nome);
      }
      if (this.tenha_nome == nome) this.tenha_nome = "";
      else this.naotenha_nome = "";
      this.$store.dispatch("basicSearch");
    },
    removeTag(tags, index) {
      tags.splice(index, 1);
      this.$store.dispatch("basicSearch");
    },
  },

  created() {
    this.$store.dispatch("fetchReceitas");
  },
};
</script>

<style scoped>
/*.v-card,
.v-text-field:not(.classificar-por) {
  border: 2px solid var(--color4) !important;
}*/
.v-card,
.v-text-field:not(.classificar-por) {
  border-radius: 2px;
}
.v-card {
  border: 2px solid var(--color1);
}
.v-text-field:not(.classificar-por) {
  border: 2px solid var(--color5);
}
div {
  background-color: var(--color4);
}
</style>
