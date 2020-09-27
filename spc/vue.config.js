// const GoogleFontsPlugin = require('google-fonts-webpack-plugin')

// const fs = require('fs')
// const https = require('https')

module.exports = {
  publicPath: './',

  // publicPath: process.env.NODE_ENV === 'production' ? '/spc/' : '/',
  outputDir: 'dist/',
  pages: {
    index: {
      entry: 'src/main.js',
    },
  },
  devServer: {
    disableHostCheck: true,
    // https: {
    //   cert: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem'),
    //   key: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem'),
    //   rejectUnauthorized: false
    // },
   // public: 'https://localhost:5005/'

  },

  transpileDependencies: ['vuetify'],
  lintOnSave: false,
}
