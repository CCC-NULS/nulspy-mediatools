import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: colors.deepPurple.lighten1, // md #7e57c2  [10% light-#9871DC]  deep-purple (was tw 805ad5)
  secondary: colors.deepPurple.accent1, // md: #b388ff  //was tw light purple b794f4
  tertiary: colors.teal.base,  //md teal  009688   
  success: colors.teal.accent4,  // md teal accent-4 00BFA5
  accent: colors.orange.lighten2,  //md orange lighten-2  FFB74D
  info: colors.grey.lighten2,  // md deep-purple accent-3  651fff
  error: colors.red.lighten1,   //md deep-purple darken-2 455A64
  warning: colors.orange.lighten2,  //md blue-grey darken-2  455A64
  darkgrey: colors.grey.darken3, // 212121
  orangetext: colors.deepOrange.lighten5, // for text
  peachy: colors.deepOrange.lighten4,
  pinkish: colors.deepPurple.lighten4,
  tealish: colors.teal.lighten4,
  greyish: colors.blueGrey.lighten4
  // purple1: primary,
  // purple2: secondary,
  // orange1: accent  // was tw f6ad55 orange400
}  // deep-purple: #9C27B0
// const deepPurple = Object.freeze({
//   base: '#673ab7',
//   lighten5: '#ede7f6',
//   lighten4: '#d1c4e9',
//   lighten3: '#b39ddb',
//   lighten2: '#9575cd',
//   lighten1: '#7e57c2',
//   darken1: '#5e35b1',
//   darken2: '#512da8',

// const dtheme = {
//   primary: colors.teal.base, // #009688
//   primarydark: colors.teal.darken1, // # 
//   secondary: colors.deepPurple.base,  // deep purple  673AB7
//   success: colors.cyan.base,   // cyan
//   accent: colors.deepOrange.lighten2,    // deep-orangeFF5722
//   info: colors.grey.base,              //   grey 
//   warning: colors.deepOrange.base,    // deep-orange
// }


export default new Vuetify({

  theme: {
    themes: {
      dark: theme,
      light: theme,
    },
  },
})

// teal=009688
 // deep purple  673AB7
 //  blue #0a406c from gradient
// #00BCD4',    // cyan
// #FF5722',    // deep-orange
//  '#F44336',   // red
// darkgrey: '#212121'
//'deep-orange lighten-5'
  // lighttext: '#FBE9E7',     //'deep-orange lighten-5 e7'

  //   primary: '#805ad5', // purple 805ad5
  // secondary: '#b794f4',  //tw light purple b794f4
  // tertiary: '#009688',  //md teal  009688
  // success: '#00BFA5',  // md teal accent-4 00BFA5
  // accent: '#FFB74D',  //md orange lighten-2  FFB74D
  // info: '#651fff',  // md deep-purple accent-3  651fff
  // error: '#512DA8',   //md deep-purple darken-2 455A64
  // warning: '#455A64',  //md blue-grey darken-2  455A64
  // darkgrey: '#212121', // 212121
  // orangetext: accent,
  // purple1: primary,
  // purple2: secondary,
  // orange1: accent  // was tw f6ad55 orange400