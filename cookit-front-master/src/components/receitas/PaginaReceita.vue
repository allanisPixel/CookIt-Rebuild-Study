<template>
  <div v-bind:key="receita.id" class="container">
    <div v-if="receita.dono_receita.visivel">
      <v-card class="mx-auto mt-5 mb-10" id="thumbnails-receita-completa">
        <div class="row">
          <img
            class="receita-foto mt-2"
            style="max-width: 80%"
            v-bind:src="receita.fotos"
            alt=""
          />
          <div id="opcoes-receita-completa" class="col-1">
            <v-btn icon color="deep-orange accent-4">
              <v-icon>mdi-heart</v-icon>
            </v-btn>

            <br />
            <v-btn icon color="blue darken-2">
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>

            <br />
            <v-btn icon color="deep-purple accent-1 lighten-2">
              <v-icon>fas fa-flag</v-icon>
            </v-btn>
            <!-- <v-icon>fas fa-flag</v-icon> -->
          </div>
        </div>

        <div class="row">
          <div id="titulo-receita-completa" class="col">
            <h3>{{ receita.nome_receita }}</h3>
            <p>
              publicado por
              <strong> {{ receita.dono_receita.first_name }} </strong>
            </p>
            <div>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
          </div>
        </div>
        <div class="col-md">
          <div class="row">
            <div class="col mb-3">
              <div id="icones-receita-completa" class="amber accent-1 col">
                <div class="col line-receita-completa" style="border: none">
                  <div class="icon-text-receita-completa">
                    <v-icon color="black">fas fa-clock</v-icon>
                    <br />
                    <p>
                      {{ receita.tempo_preparo }}
                      {{ receita.tempo_unidade_medida }}
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <v-icon color="">mdi-pizza</v-icon>
                    <br />
                    <p>
                      {{ receita.porcoes }}
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <v-icon color="blue-grey darken-4"
                      >fas fa-tachometer-alt</v-icon
                    >
                    <br />
                    <p>
                      {{ receita.dificuldade }}
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <v-icon color="deep-orange accent-4">fas fa-heart</v-icon>

                    <br />
                    <p>Favoritos</p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <v-icon color="blue darken-2">mdi-message-text</v-icon>
                    <br />
                    <p>Comentários</p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <v-icon color="black">fas fa-calendar-alt</v-icon>
                    <br />
                    <p>{{ receita.data_publicacao }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </v-card>

      <div class="row">
        <v-card
          class="mx-auto"
          color="white"
          dark
          max-width="540"
          min-width="540"
        >
          <v-card-text class="text-h5 font-weight-bold">
            <h3
              class="black--text d-flex justify-content-center font-weight-bold"
            >
              Ingredientes
            </h3>
            <v-btn
              elevation="2"
              raised
              rounded
              text
              class="orange darken-3 white--text mt-2"
              v-for="ingrediente in receita.ingredientes"
              :key="ingrediente.id"
            >
              <p class="font-weight-bold mt-3">
                {{ ingrediente.nome_ingrediente }}
                {{ ingrediente.quantidade_ingrediente }}
                {{
                  formatUnidadMedIngred(ingrediente.unidade_medida_ingrediente)
                }}
              </p>
            </v-btn>
          </v-card-text>
        </v-card>

        <v-card
          class="mx-auto"
          color="white"
          dark
          max-width="540"
          min-width="540"
          min-height="200"
        >
          <v-card-text class="black--text text-justify">
            <h3
              class="black--text d-flex justify-content-center font-weight-bold"
            >
              Modo de preparo
            </h3>
            <p class="font-weight-bold">{{ receita.modo_preparo }}</p>
          </v-card-text>
        </v-card>
      </div>
      <v-card class="mt-10" style="height: 100px">
        <div>
          

          

          <v-btn
            depressed
            class="publish yellow darken-3 font-weight-bold black--text"
            style="margin-top: -500px"
            @click="$router.push({name: 'EditarReceita', params: {id: receita.id}})"
            >Editar Receita</v-btn
          >


        </div>
      </v-card>
    </div>

    <div class="dados-receita-completa" v-else>
      <h1>Desculpe! :(</h1>
      <p>Esta receita não existe ou foi excluída.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";
import moment from "moment";
import "moment/locale/pt-br";

export default {
  data() {
    return {
      receita: "",
      unitingred: "",
      sabereceita: "",
      temppreparo: "",
      categreceita: "",
      dificultreceita: "",
    };
  },
  mounted() {
    this.getReceita();
  },
  methods: {
    getReceita() {
      axios.get("/api/receita/" + this.$route.params.id).then((response) => {
        this.receita = response.data;
        this.receita.data_publicacao = this.format_date(
          this.receita.data_publicacao
        );
      });
    },

    ...mapActions(["deleteReceita"]),

    format_date(value) {
      if (value) {
        return moment(String(value)).format(
          "DD [de] MMMM [de] YYYY, [às] h:mm"
        );
      }
    },

    formatUnidadMedIngred(data) {
      this.unitingred = this.$store.state.receitas.umedingrediente;
      this.unitingred.forEach((i) => {
        if (data == i.letra) {
          console.log(i.valor);
          data = i.valor;
        }
      });
      return data;
    },

    formatSaborReceita(data) {
      this.sabereceita = this.$store.state.receitas.saborreceita;
      this.sabereceita.forEach((i) => {
        if (data == i.letra) {
          console.log(i.valor);
          data = i.valor;
        }
      });
      return data;
    },
    formatTempoPreparo(data) {
      this.temppreparo = this.$store.state.receitas.tempopreparo;
      this.temppreparo.forEach((i) => {
        if (data == i.letra) {
          console.log(i.valor);
          data = i.valor;
        }
      });
      return data;
    },
    formatCategoriaReceita(data) {
      this.categreceita = this.$store.state.receitas.categoriareceita;
      this.categreceita.forEach((i) => {
        if (data == i.letra) {
          console.log(i.valor);
          data = i.valor;
        }
      });
      return data;
    },
    formatDificuldadeReceita(data) {
      this.dificultreceita = this.$store.state.receitas.categreceita;
      this.categreceita.forEach((i) => {
        if (data == i.letra) {
          console.log(i.valor);
          data = i.valor;
        }
      });
      return data;
    },
  },
};
</script>

<style scoped>
/* .container {
  margin: 0 auto;
  margin-top: 80px;
  border-left: 1px solid #707070;
  border-right: 1px solid #707070;
} */

.dados-receita-completa {
  background-color: white;
  border: 1px solid grey;
  border-radius: 1em;
  margin: 1em;
  padding: 1em;
}
#titulo-receita-completa {
  text-align: center;
}
#titulo-receita-completa h3 {
  color: #dd2c00;
}
#opcoes-receita-completa {
  display: flex;
  align-items: center;
  flex-direction: column;
}
#icones-receita-completa {
  border: 1px solid #707070;
  background-color: #f3efef;
  border-radius: 0.1em;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 1em;
}
.icon-text-receita-completa {
  text-align: center;
  max-width: 7em;
}
.icon-text-receita-completa i {
  font-size: 2em;
}
.icon-text-receita-completa p {
  margin-bottom: 0;
}

.line-receita-completa {
  border-left: 1px solid black;
  height: 65px;
  width: 16.6%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.fa-star {
  color: orange;
}
.receita-foto {
  object-fit: cover;
  /* Do not scale the image */
  object-position: center;
  /* Center the image within the element */
  width: 500%;
  height: 200px;
  margin-left: 100px;
  margin-bottom: 1rem;
  background: #707070;
  border: 1px solid #707070;
}

.publish {
  margin: 0;
  position: absolute;
  top: 95.4%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>