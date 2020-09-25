<template>
  <v-footer
    id="footer"
    height="65px"
    :style="`background-image: linear-gradient(306deg, #BDBDBD, #D7D7D7 )`"
    app
  >
    <v-container>
      <v-row
        align="center"
      >
        <v-col
          v-for="(link, i) in links"
          :key="i"
          class="text-center heading"
          cols="auto"
        >
          <a
            :href="link.href"
            rel="noopener"
            target="_blank"
            v-text="link.text"
          />
        </v-col>

        <v-spacer />

        <v-col
          cols="12"
          md="auto"
        >
          <div class="body-1 font-weight-600 pt-2 pt-md-0 text-center">
            &copy; 2020, made with
            <v-icon
              size="14"
              color="red"
            >
              mdi-heart
            </v-icon>
            by <a href="https://nuls.io">NULS</a> for a better blockchain.
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',

  data: () => ({
    links: [
      {
        href: 'http://nuls.io',
        text: 'NULS'
      },
      {
        href: 'http://nuls.io',
        text: 'About Us'
      },
      {
        href: 'http://nuls.io',
        text: 'Blog'
      },
      {
        href: 'http://nuls.io',
        text: 'Licenses'
      }
    ]
  })
}
</script>

<style lang="sass">
  #dashboard-core-footer
    a
      font-size: 14px
      text-decoration: none
      text-transform: uppercase

.v-footer
  padding: 2px 0 2px 4px
  border-top: 0px solid #e7e7e7
  position: relative
  a
    padding: 5px 6px 5px 6px
    font-size: 14px !important

  .body-1
    font-size: 14px !important
    padding-right: 18px
    letter-spacing: 0px !important
    a
      color: teal !important
      padding: 0
      text-transform: inherit !important
      font-size: 14px !important

  .v-icon
    margin-top: -3px

  &.v-footer--absolute
    position: absolute !important

.theme--light.v-footer
  background-color: transparent
  .body-1
    color: teal
  .v-icon
    color: #3c4858
</style>
