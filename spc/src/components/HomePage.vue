/* eslint-disable vue/name-property-casing */
<template>
  <div
    id="frontpage"
  >
    <v-row>
      <v-col
        cols="12"
        md="12"
        xs="4"
        class="d-flex flex-column justify-center align-center"
      >
        <div
          v-if="$store.state.gShowHomeBool"
          id="gethiderdiv"
          :key="$store.state.gHomeKeyCount"
        >
          <v-card
            id="mainfcard"
            flat
            class="d-none d-md-flex flex-column justify-center align-center"
            width="95%"
          >
            <v-card
              id="groupcard"
              mainfcard
              class="d-inline-flex justify-center align-center font-weight-black"
              flat
              width="640px"
              min-width="350px"
            >
              <v-card
                id="tinycardtop"
                groupcard
                width="320"
                color="#4DC0B5"
                class="d-flex text-h2 pa-2 white--text ma-5 justify-center align-center font-weight-black"
              >
                Genuine
              </v-card>
              <v-card
                id="tinycardtop"
                groupcard
                flat
                width="320"
                min-width="220"
                color="transparent"
                class="d-flex align-center text-h1 black--text justify-center"
                style="font-weight:900;"
              >
                Reviews
              </v-card>
            </v-card>
            <br>
            <span
              class="deep-orange--text text--lighten-1 mt-n11 mb-n11 font-weight-black"
              style="z-index:99;font-size:5rem;"
            >
              in
            </span>
            <br>
            <v-card
              id="groupcard2"
              mainfcard
              class="d-inline-flex flex-row align-center justify-center mt-n9"
              flat
              width="740px"
            >
              <span
                class="teal--text text--darken-1 pa-2 font-weight-black"
                style="font-size: 4rem;"
              >
                the
              </span>
              <v-card
                id="tinycard"
                color="black"
                height="100px"
                width="350px"
                elevation-22
                class="d-flex flex-row align-center justify-center white--text pa-2 font-weight-black"
                style="border-radius:0.25rem;font-size:4rem;"
              >
                blockchain
              </v-card>
            </v-card>
          </v-card>
          <v-card
            id="groupcard3"
            mainfcard
            class="d-flex flex-column align-center justify-center px-12 mt-10 mb-9"
            flat
            color="transparent"
            width="100%"
          >
            <span
              class="grey--text darken-5 text-md-h4 align-center justify-center"
              style="line-height:1.25;font-align:center;text-align:center; font-justify:center;"
              :style="`styleObject5`"
            >
              Space Exploration provides users with genuine reviews validated by the blockchain
            </span>
            <span
              style="text-align:center;font-weight:800;font-size:3rem;margin-bottom:22px;"
            >
              Try Space Exploration
            </span>
          </v-card>
          <v-card
            id="spacercard"
            mainfcard
            height="50px"
            min-height="25px"
            width="100%"
            flat
            class="d-flex flex-row justify-center align-center"
          >
            <v-card
              id="colorcard"
              spacercard
              flat
              height="59px"
              width="100%"
              class="d-flex justify-center align-center"
              :style="`background-image: linear-gradient(60deg, #009688, #00BFA5)`"
            />
          </v-card>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data: () => ({
    x: 0
  }),
  computed: {
    styleObject5 () {
      return (window.outerWidth < 960) ? { fontSize: '16px' } : { fontSize: '34px' }
    }
  },
  methods: {
    showhomebool () {
      return this.getgShowHomeBool
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital@1&display=swap');

  .leading-relaxed {
    line-height: 1.625;
  }
  .w-1 {
    width: 0.25rem;
  }
  .w-2 {
    width: 0.5rem;
  }
</style>
