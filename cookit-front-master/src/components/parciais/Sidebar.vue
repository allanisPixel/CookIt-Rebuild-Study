<template>
  <v-navigation-drawer
    v-model="$store.state.drawer"
    app
    clipped
    background-color="var(--color3)"
  >
    <v-list dense nav>
      <v-list-item>
        <v-select
          v-model="$store.state.receitas.pesquisa.dificuldade"
          :items="dificuldade"
          item-text="name"
          item-value="value"
          label="Dificuldade"
          dense
          rounded
          hide-details
          background-color="white"
          solo
          @change="$store.dispatch('basicSearch')"
        >
        </v-select>
      </v-list-item>
      <v-list-item>
        <v-card-title class="pa-0">Sabor</v-card-title>
      </v-list-item>
      <v-list-item v-for="s in sabor" :key="s.value">
        <v-checkbox
          :label="`${s.name}`"
          :value="s.value"
          dense
          hide-details
          v-model="$store.state.receitas.pesquisa.sabor_receita"
          @change="$store.dispatch('basicSearch')"
        ></v-checkbox>
      </v-list-item>
      <v-list-item>
        <v-card-title class="pa-0">Categoria</v-card-title>
      </v-list-item>
      <v-list-item v-for="c in categoria" :key="c.value">
        <v-checkbox
          :label="`${c.name}`"
          :value="c.value"
          dense
          hide-details
          v-model="$store.state.receitas.pesquisa.categoria"
          @change="$store.dispatch('basicSearch')"
        ></v-checkbox>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Sidebar",

  data() {
    return {
      dificuldade: [
        {
          value: "",
          name: "Dificuldade",
        },
        {
          value: "F",
          name: "Fácil",
        },
        {
          value: "M",
          name: "Médio",
        },
        {
          value: "D",
          name: "Dificil",
        },
        {
          value: "C",
          name: "Master Chef",
        },
      ],
      sabor: [
        {
          name: "Doce",
          value: "D",
        },
        {
          name: "Salgado",
          value: "S",
        },
      ],
      categoria: [
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
    };
  },
};
</script>

<style scoped>
v-label {
  font-size: 12px !important;
}
.v-navigation-drawer {
  background-color: var(--color4) !important;
}
.v-label {
  font-size: 2em !important;
}
.v-text-field {
  border: 2px solid var(--color5);
}
</style>