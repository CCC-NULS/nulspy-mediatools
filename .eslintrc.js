module.exports = {
  root: true,

  env: {
    node: true,
  },

  extends: 'vuetify',

  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
	  'camelcase': 'off',
    '@typescript-eslint/camelcase': ['off']
	//'camelcase': [
    //  2, {
    //    'properties': 'never'
    //  }
   // ],
  },

  parserOptions: {
    parser: 'babel-eslint',
  },

  'extends': 'plugin:vue/recommended'
}
