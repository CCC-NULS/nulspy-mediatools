<template>
  <v-card
    id="chipgray"
    v-bind="cardyprops2"
    class="d-flex flex-column align-center align-content-center white--text montyfont px-3 mx-3 py-1 mt-n3"
    :style="`position:relative;z-index:4;font-size:15px;font-weight:500;`"
  >
    {{ tlabel }}
  </v-card>
</template>

<script>
export default {
  name: 'ChipGray',
  props: {
    tlabel: {
      type: String,
      default: 'chip',
      required: false
    }
  },
  data: () => ({
    cardyprops2: {
      width: '190px',
      height: '34px',
      'max-width': '190px',
      'min-width': '120px',
      'min-height': '20px',
      'max-height': '550px',
      color: 'blue-grey darken-2',
      dark: true
    }
  })
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=PT+Sans+Narrow&display=swap');

  .montyfont {
    font-family: 'Montserrat',sans-serif;
    letter-spacing: 1.25px;
    text-transform: lowercase;
  }
</style>
tag: {
      type: String,
      required: false,
      default: 'i'
    }
