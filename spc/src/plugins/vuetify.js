import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: colors.deepPurple.lighten1, // md #7e57c2  [10% light-#9871DC]  deep-purple (was tw 805ad5)
  secondary: colors.deepPurple.accent1, // md: #b388ff  //was tw light purple b794f4
  tertiary: colors.teal.base, // md teal  009688
  success: colors.teal.accent4, // md teal accent-4 00BFA5
  accent: colors.orange.lighten2, // md orange lighten-2  FFB74D
  info: colors.grey.lighten2, // md deep-purple accent-3  651fff
  error: colors.red.lighten1, // md deep-purple darken-2 455A64
  warning: colors.orange.lighten2, // md blue-grey darken-2  455A64
  darkgrey: colors.grey.darken3, // 212121
  orangetext: colors.deepOrange.lighten5, // for text
  peachy: colors.deepOrange.lighten4,
  pinkish: colors.deepPurple.lighten4,
  tealish: colors.teal.lighten4,
  greyish: colors.blueGrey.lighten4
} 

export default new Vuetify({
  theme: {
    themes: {
      dark: theme,
      light: theme
    }
  }
})
