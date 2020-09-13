<template>
  <v-container
    id="appybar"
    fluid
  >
    <v-app-bar
      id="app-bar-comp"
      app
      :height="vheight"
      v-bind="abprops"
      shrink-on-scroll
      class="d-none d-md-inline-flex mb-2 justify-between align-bottom pb-3"
      :style="`background-image: linear-gradient(60deg, #008080, black);`"
    >      
      <v-toolbar-title
        id="appbartitle"
        class="white--text mb-2"
        :style="`font-family:Montserrat,sans-serif;font-size:27px;`"
      >
        Welcome to Space Exploration
      </v-toolbar-title>
      <v-card
        id="myspacer"
        width="300px"
        height="20px"
        color="transparent"
        class="align-self-end"
      />
      <v-btn
        id="navbtn1"
        color="blue-grey darken-1"
        v-bind="btnprops"        
        class="d-flex montyfontb align-self-end justify-self-end my-4 ml-10"
        to="/"
        @click="homeclick"
      >
        Home
      </v-btn>
      <v-btn
        id="navbtn2"
        v-bind="btnprops"        
        class="d-flex montyfontb align-self-end justify-self-end my-4 ml-10" 
        to="AllReviews"
        @click="allrevsclick"
      >
        Reviews
        <v-icon
          style="font-size:36px;margin-left:12px;"
          color="white"
        >
          mdi-rocket-outline
        </v-icon>
      </v-btn>
    </v-app-bar>
    <!-- following is for mobile only -->
    <div 
      d-xs-flex 
      d-md-none 
      flex-inline-row
    >
      <v-btn
        id="navbtn3"
        :width="btnwidth"
        color="blue-grey darken-1"
        v-bind="btnprops"        
        class="d-xs-flex d-md-none montyfontb mt-2"
        to="/"
        @click="homeclick"
      >
        Home
      </v-btn>
      <v-btn
        id="navbtn4"
        color="teal darken-1"
        v-bind="btnprops"        
        class="d-xs-flex d-md-none montyfontb mt-2 ml-3"
        to="AllReviews"
        @click="allrevsclick"
      >
        Reviews
        <v-icon
          style="font-size:26px;margin-left:10px;"
          color="white"
        >
          mdi-rocket-outline
        </v-icon>
      </v-btn>
    </div>
  </v-container>
</template>

<script>
  import { mapState, mapMutations, mapActions, mapGetter } from "vuex";
  import store from  '../store'

  export default {
    name: 'AppyBar',
    data: () => ({
      homekey: 0,
      btnprops: {
        height: "45px",
        "min-width": "40px",
        "min-height": "20px",        
        "max-width": "220px",
        "max-height": "120px", 
        dark: true,
        medium: true,
        color: "blue-grey",        
      },
      abprops: {
        width: "100%",
        "min-width": "140px",
        "max-width": "2000px",      
        "min-height": "0px",
        "max-height": "250px",
        elevation: 12,
        prominent: false,
        dark: true,
      }
    }),
    computed: {
      newHomeKeyCt () {
        return this.$store.state.gHomeKeyCount
      },
      vheight () {
        return window.outerWidth > 959 ? '120px' : '2px';
        },
      btnwidth () {
        return window.outerWidth > 959 ? '220px' : '100px';
        },
    },
    methods: {
      homeclick () {
        let newcount = this.newHomeKeyCt 
        newcount += 1;
        this.$store.dispatch('gShowHomeBoolAct', true)   // show home page
        this.$store.dispatch('gShowAllrevsAct', false)  // hide reviews
        this.$store.dispatch('gHomeKeyCountAct', newcount)  // up the number
      },  
      allrevsclick () {
        let newcount = this.newHomeKeyCt 
        newcount += 1;        
        this.$store.dispatch('gShowHomeBoolAct', false)
        this.$store.dispatch('gShowAllrevsAct', true)
        this.$store.dispatch('gHomeKeyCountAct', newcount)
      }, 
    },    
  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
  .montyfontb {
    font-size: 18px;
    color: white;
    font-family: 'Montserrat',sans-serif;
    letter-spacing: 1.25px;
    text-transform: lowercase;
  }
  .v-toolbar__title {
    white-space: pre-wrap;
  }
</style>
