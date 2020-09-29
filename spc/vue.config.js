// import https from 'https'
const fsx = require('fs-extra')

module.exports = {
publicPath: '/spc/',
  outputDir: 'dist/',
  pages: {
    index: {
      entry: 'src/main.js',
    },
  },
  devServer: {
    disableHostCheck: true,
    https: {
      cert: fsx.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem'),
      key: fsx.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem'),
    },
   public: 'https://localhost:5005/',
  },
  transpileDependencies: ['vuetify'],
  lintOnSave: false,
}

