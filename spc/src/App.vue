<template>
  <v-app id="app">
    <AppyBar
      app
    />
    <v-main>
      <v-container fluid>
        <router-view />
        <AllReviews
          v-if="$store.state.gShowAllrevs"
          :key="$store.state.gHomeKeyCount"
        />
      </v-container>
    </v-main>
    <Footer app />
  </v-app>
</template>

<script>
// see https://vuetifyjs.com/en/components/application/ for detailed instructions for this component
import AllReviews from './components/AllReviews'
import AppyBar from './components/AppyBar'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    AppyBar,
    AllReviews,
    Footer
  }
}
</script>
