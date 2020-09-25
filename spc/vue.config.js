
const GoogleFontsPlugin = require("google-fonts-webpack-plugin");

const fs = require('fs')
const https = require('https')

module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/spc/' : '/',
  outputDir: 'dist/',
  devServer: {
    https: {
      cert: fs.readFileSync("/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem"),
      key: fs.readFileSync("/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem"),
      rejectUnauthorized: false
    },
  public: 'https://localhost:5004/',
  },
  transpileDependencies: ['vuetify'],
  chainWebpack: config => {
    plugins: [
      new GoogleFontsPlugin({
        fonts: [
          { family: "Rubik" },
          { family: "Montserrat" },
          { family: "Raleway" },
          { family: "PT Sans Narrow" },
        ]
      })
    ]
  },
  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false,
    },
  },
}

