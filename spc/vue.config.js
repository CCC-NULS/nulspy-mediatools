// https://cli.vuejs.org/config

module.exports = {
  publicPath: '/spc/',
  devServer: {
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

