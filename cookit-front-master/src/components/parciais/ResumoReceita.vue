<template>
  <v-card class="" v-bind:key="receita.id">
    <a
      @click="
        $router.push({ name: 'PaginaReceita', params: { id: receita.id } })
      "
      name="button-detail"
    >
      <v-img
        v-if="receita.fotos != null"
        height="180"
        v-bind:src="receita.fotos"
      >
      </v-img>
      <v-sheet
        class="d-flex justify-center align-center"
        v-else
        color="var(--color1)"
        height="180"
      >
        <v-sheet
          class="rounded-circle d-flex justify-center align-center"
          height="90"
          width="90"
          color="white"
        >
          <v-icon color="var(--color1)" large>fas fa-utensils</v-icon>
        </v-sheet>
      </v-sheet>
    </a>
    <a
      @click="
        $router.push({ name: 'PaginaReceita', params: { id: receita.id } })
      "
      ><v-card-title class="pb-0"> {{ receita.nome_receita }} </v-card-title></a
    >
    <v-card-text>
      <v-row align="center" class="mx-0">
        <p class="mb-0">
          por
          <a href=""
            ><strong
              >{{ receita.dono_receita.first_name }}
              {{ receita.dono_receita.last_name }}</strong
            ></a
          >
        </p>
        <v-spacer></v-spacer>
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>
        <!--<div class="grey--text ms-4">4.5 (413)</div>-->
      </v-row>
    </v-card-text>
    <v-divider class="mx-4 my-0"></v-divider>
    <v-card-text
      class="mb-0 pb-0"
      v-for="ingrediente in receita.ingredientes"
      :key="ingrediente.id"
    >
      <v-chip
        color="var(--color5)"
        text-color="white"
        x-small
        class="mr-2 mb-2"
        >{{ ingrediente.nome_ingrediente }}</v-chip
      >
    </v-card-text>
    <v-divider class="mx-4 my-0"></v-divider>
    <v-card-text class="dados text-center">
      <v-row>
        <v-col>
          <v-icon> fas fa-clock</v-icon>
          <p>{{ receita.tempo_preparo }} {{ receita.tempo_unidade_medida }}</p>
        </v-col>
        <v-col>
          <v-icon> fas fa-tachometer-alt</v-icon>
          <p>{{ receita.dificuldade }}</p>
        </v-col>
        <v-col>
          <v-icon> fas fa-lemon</v-icon>
          <p>{{ receita.sabor_receita }}</p>
        </v-col>
        <v-col>
          <v-icon> fas fa-layer-group</v-icon>
          <p>{{ receita.categoria }}</p>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "ResumoReceita",
  props: {
    receita: Object,
  },
};
</script>

<style>
.dados p {
  font-size: 10px;
}
</style>