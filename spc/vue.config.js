// const GoogleFontsPlugin = require('google-fonts-webpack-plugin')

const fs = require('fs')
// import https from 'https'

module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/spc/' : '/',
  outputDir: 'dist/',

  devServer: {
    disableHostCheck: true,
    https: {
      cert: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem'),
      key: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem'),
      rejectUnauthorized: false,
    },
    public: 'https://localhost:5005/',
  },
  transpileDependencies: ['vuetify'],
  lintOnSave: false,
}
