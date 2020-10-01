
const GoogleFontsPlugin = require("google-fonts-webpack-plugin");
// const isProduction = process.env.NODE_ENV === 'production';
// publicPath really needs to be /spc/ or something

module.exports = {
  // publicPath: '/spc/',
  devServer: {
    port: 5007,
    host: '127.0.0.1',
    disableHostCheck: true,
  },
  transpileDependencies: [
    'vuetify'
  ],
  runtimeCompiler: true,
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
  }
 }

