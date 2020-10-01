
const GoogleFontsPlugin = require("google-fonts-webpack-plugin");
// const isProduction = process.env.NODE_ENV === 'production';
// publicPath really needs to be /spc/ or something

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/spc/'
    : '/'
  devServer: {
    port: 5004,
    host: '0.0.0.0',
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

