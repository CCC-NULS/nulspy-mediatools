<template>
  <v-row>
    <!-- top level col -->
    <v-col
      cols="12"
      md="6"
      class="d-flex flex-column"
    >
      <!-- * * * * * * * ENTIRE LEFT COLUMN card on left -->
      <v-card
        id="columncard-left"
        color="transparent"
        width="100%"
        height="auto"
        min-width="200px"
        max-width="700px"
        min-height="550px"
        max-height="1200px"
        elevation-24
        raised
        shaped
        filled
        class="d-flex flex-column align-center flex-shrink-1 pt-1 pb-3 mt-0"
      >
        <!-- * * * * * * *  card on left -->
        <v-card
          id="top-backcard"
          color="transparent"
          flat
          columncard-left
          width="100%"
          height="70px"
          min-width="23px"
          max-width="900px"
          min-height="90px"
          max-height="907px"
          class="d-flex flex-column mx-3 mt-1 mb-1"
        >
          <!-- JUST THE LABEL TITLE WORD CONTRACT: -->

          <v-card
            v-for="contract in contracts"
            id="contractviewer"
            :key="contract"
            color="transparent"
            width="breakpoint.smAndDown ? 200px : 600px"
            flat
            height="140px"
            min-height="110px"
            max-height="290px"
            max-width="600px"
            min-width="100px"
            class="d-flex flex-inline-row flex-grow-1 pa-0 mt-0 mb-5 mx-0 ptsans"
          >
            <v-chip
              id="titleChiptopContract"
              color="transparent"
              text-color="black"
              contractviewer
              label
              large
              class="montyfont px-3 mx-2 mb-n1"
              style="font-size:16px;font-weight:700;"
            >
              <v-icon
                :style="`margin-right:10px;`"
              >
                mdi-nfc
              </v-icon>
              <span
                style="margin-right:10px;"
              >
                contract:
              </span>
              <span
                :style="styleContract"
                style="text-transform:none;"
                class="ptsans"
              >
                {{ contract }}
              </span>
            </v-chip>

            <!--  card CHIP with contract # very small - - - -   -->
          </v-card> <!-- end contractchip -->
        </v-card>  <!-- form card start -->
        <v-card
          id="form-card"
          color="teal lighten-5"
          columncard-left
          width="92%"
          min-width="250px"
          max-width="700px"
          min-height="300px"
          shaped
          :style="computedHeight"
          class="d-flex flex-column align-center px-0 pt-2 pb-2 mx-1 mt-3 mb-7"
        >
          <v-chip
            id="write-rev-Chip"
            color="transparent"
            text-color="black"
            vselbackgroundcard2
            label
            dark
            medium
            class="montyfont textlow pl-2 py-6 mx-3 mt-1 mb-1 text-center"
            style="font-size:36px;font-weight:700;max-width:600px;"
          >
            <v-icon
              :style="`margin-right:22px;font-size:36px;line-height:50px;`"
            >
              mdi-rocket-launch
            </v-icon>
            write review
          </v-chip>

          <v-card
            id="form-wrap"
            form-card
            width="475px"
            height="430px"
            min-width="420px"
            max-width="600px"
            min-height="200px"
            max-height="400px"
            flat
            color="transparent"
            class="d-flex flex-column align-center justify-center flex-grow-1 flex-shrink-1 pa-1 ma-1"
          >
            <v-form
              id="wform"
              ref="wform"
              form-wrap
              background-color="white"
              width="470px"
              min-width="270px"
              max-width="650px"
              min-height="300px"
              max-height="900px"
              class="d-flex flex-column flex-grow-1 flex-shrink-1 justify-center align-center mt-5 mx-1 pa-2"
              @submit.prevent="submit"
            >
              <v-text-field
                id="textfieldform1a"
                v-model="vmcat"
                height="auto"
                width="250px"
                min-width="200px"
                max-width="220px"
                min-height="50px"
                max-height="200px"
                required
                clearable
                color="deep-purple"
                label="Product Category"
                class="pa-2 mb-0 mx-2"
                :style="styleTextareaSz"
              />
              <v-textarea
                id="textfieldform1b"
                v-model="vmrev"
                label="Your Review"
                color="deep-purple"
                height="110px"
                min-width="270px"
                max-width="700px"
                min-height="100px"
                max-height="300px"
                outlined
                clearable
                class="pa-2 ma-2"
                :style="styleTextareaSz"
              />
              <v-card
                id="tocenterbutton"
                form-wrap
                flat
                color="transparent"
                width="100%"
                height="10px"
                class="d-flex flex-column align-center justify-center"
              >
                <v-card-actions>
                  <v-btn
                    id="wrevbtn"
                    dark
                    tocenterbutton
                    elevation-12
                    color="deep-orange darken-2"
                    class="mt-n4 mb-3 montyfont textlow"
                    style="text-transform:lowercase;"
                    @click="wreview"
                  >
                    submit review
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-card>
        </v-card>  <!-- end formAREA --><!-- begin feedback -->
        <v-card
          id="feedbackcard"
          columncard-left
          color="transparent"
          width="auto"
          height="60px"
          min-width="320px"
          max-width="620px"
          min-height="50px"
          max-height="100px"
          flat
          class="d-flex flex-column flex-grow-1 align-center px-0 pt-0 mx-0 mt-3 mb-3"
        >
          <v-simple-table
            id="feedbacktable"
            feedbackcard
            color="teal lighten-2"
            width="auto"
            height="auto"
            min-width="220px"
            max-width="620px"
            min-height="40px"
            max-height="2050px"
            class="d-flex flex-column flex-grow-1 px-2 py-1"
          >
            <span
              id="writeresspan"
              :key="writeresultkey"
              style="font-size:14px;"
            >
              <pre>{{ writeresult }}</pre>
            </span>
          </v-simple-table>
        </v-card>  <!-- end formAREA -->
      </v-card>  <!-- end formcardtwo -->
    </v-col>
    <!-- </v-col> -->
    <!-- end product card  * * * * * * * END LEFT COLUMN * * * * * * * * * * * * * * * * * * * * * * * -->
    <v-col
      cols="12"
      md="6"
      class="d-flex flex-column"
    >
      <!-- ****** column card  -->
      <v-card
        id="columncard-right"
        color="white"
        width="100%"
        height="auto"
        min-height="250px"
        max-height="3000px"
        elevation-24
        raised
        shaped
        filled
        class="d-flex flex-column flex-grow-1 align-center pt-2"
      >
        <!--   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * -->
        <!-- ****** vsel RED groupcard  -->
        <v-card
          id="groupcard"
          columncard-right
          width="100%"
          height="yesbig ? '450px' : '650px'"
          min-height="275px"
          max-height="3000px"
          flat
          color="transparent"
          class="d-flex flex-column flex-grow-1 flex-shrink-1 align-center mt-1 px-3"
        >
          <!-- * * * * * * vselbackgroundcard select BACKGROUND  -->

          <v-card
            id="vselbackgroundcard2"
            :key="prodkey"
            groupcard
            width="97%"
            height="100%"
            min-width="150px"
            max-width="600px"
            min-height="170px"
            max-height="330px"
            color="transparent"
            class="d-flex flex-column flex-grow-1 align-center flex-shrink-1 px-2 py-6 mx-1 my-6"
          >
            <!-- * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * *  -->
            <!-- * * * * * *  * * * * * * * PRODUCT CHOICE SELECT * * * * * * * * * * * * * * * * *  -->
            <v-chip
              id="reviews-titleChipTop"
              color="transparent"
              text-color="black"
              vselbackgroundcard2
              label
              large
              class="montyfont textlow px-3 mx-2 mb-n1 mt-n1"
              style="font-size:36px;font-weight:700;"
            >
              <v-icon
                :style="`margin-right:12px;font-size:36px;`"
              >
                mdi-layers-search
              </v-icon>
              <span
                style="margin-right:24px;"
              >
                read reviews <br>
              </span>
            </v-chip>
            <v-select
              id="vselone"
              :key="showprodkey"
              ref="vselone"
              v-model="prodchoice"
              vselbackgroundcard2
              label="Select a Product then press Go"
              color="deep-purple accent-3"
              width="82%"
              height="30px"
              min-width="100px"
              max-width="450px"
              min-height="30px"
              max-height="160px"
              :items="productlist"
              class="d-flex mt-2 mb-0 ml-2 mr-10 pr-2"
            />
            <!--  -->
            <v-card
              id="btnspacer"
              color="transparent"
              width="100%"
              height="150px"
              flat
              class="d-flex flex-column justify-center align-center"
            >
              <v-card-actions>
                <v-btn
                  id="getrevssbtn"
                  color="deep-orange darken-2"
                  dark
                  vselbackgroundcard2
                  elevation-12
                  class="mb-5 montyfont textlow"
                  style="text-transform:lowercase;"
                  @click="axiosGetRevs"
                >
                  go
                </v-btn>
              </v-card-actions>
              <span
                style="font-size:12px;margin-top:24px;"
              >
                If your product isn't showing in the list, try the reload products button.
              </span>
              <v-card-actions>
                <v-btn
                  id="reloadbtn"
                  color="cyan darken-4"
                  outlined
                  small
                  vselbackgroundcard2
                  class="d-flex mb-3 mt-2 align-self-right"
                  style="text-transform:lowercase;"
                  @click="reloadProducts"
                >
                  <span
                    style="font-size:12px;"
                  >
                    reload products
                  </span>
                </v-btn>
              </v-card-actions>
            </v-card>  <!-- end vselbackgroundcard -->
          </v-card>  <!-- end vselbackgroundcard -->
          <!-- end select a product -->
        </v-card>      <!-- end greencard -->
        <!-- ******end green card -->
        <!-- ****** column 2 -->
        <!-- ****** data results - revs listed here -->
        <v-card
          id="spacercard3"
          height="12px"
          width="100%"
          min-width="100%"
          flat
          color="transparent"
        />
        <v-card
          id="reviewssheet"
          columncard-right
          color="teal lighten-5"
          height="auto"
          width="92%"
          min-width="170px"
          min-height="150px"
          :max-width="`styleobject4`"
          max-height="3000px"
          shaped
          class="d-flex flex-column align-left flex-grow-1 flex-shrink-1 px-6 pt-3 pb-6 mx-6 mt-4 mb-10"
        >
          <v-card
            id="chipdivcenter"
            color="transparent"
            width="100%"
            height="70px"
            min-height="70px"
            class="d-flex flex-column align-center pa-0 ma-0"
            flat
          >
            <v-chip
              id="reviewsChip"
              chipdivcenter
              color="transparent"
              text-color="black"
              large
              label
              medium
              class="montyfont textlow textlow px-6 pt-3 pb-0 mx-3 mt-1 mb-0 text-center"
              style="font-size:30px;font-weight:700;max-width:200px;"
            >
              <v-icon
                :style="`margin-right:12px;font-size:36px;`"
              >
                mdi-clipboard-flow
              </v-icon>
              reviews
            </v-chip>
          </v-card>
          <!-- Math.random below is for duplicate keys problem -->
          <v-simple-table
            v-for="reviewitm in reviewlist"
            id="reviewstable"
            :key="reviewitm.id + Math.random().toString()"
            reviewssheet
            dense
            height="auto"
            width="auto"
            :max-width="`styleObject4`"
            min-width="120px"
            min-height="37px"
            max-height="1550px"
            class="d-flex flex-column flex-grow-1 flex-shrink-1 pa-3 ml-1 mr-4 mt-1 mb-1"
          >
            <span :style="`font-size:14px;overflow-x:scroll;`"> {{ reviewitm.comments }} </span>
          </v-simple-table>
        </v-card>   <!-- end rightbtmsheet -->
      </v-card>  <!-- end   botdivgraphic -->
    </v-col>
  </v-row>
</template>

<script>
  /* eslint-disable vue/max-attributes-per-line */
  import { axiosGetProducts, writeReview, axiosGetReviewsMain } from './queries.js'
  const dJSON = require('dirty-json')
  import { cobj }  from '@/constants/dataConstants.js'
  const tchainid = cobj.chainid
  const contractaddy = cobj.contaddy
  const myurl3 = cobj.url3

  async function axiosGetRevs () {
    const productChoice = this.prodchoice
    console.log('inside AllReviews.vue function axiosGetRevs ')
    console.log('using westUrl3: ' + myurl3 + ' tchainid: ' + tchainid)
    console.log('getting productChoice: ' + productChoice + ' contract: ' + contractaddy)

    const theGetResponse = await axiosGetReviewsMain(tchainid, contractaddy, productChoice, myurl3)
    console.log('theGetResponse: ' + theGetResponse)

    const myresult = theGetResponse.data.result.result // step 1 stringify
    console.log('theGetResponse.data: ' + theGetResponse.data)
    console.log('theGetResponse.data.result: ' + theGetResponse.data.result)
    console.log('theGetResponse.data.result.result: ' + theGetResponse.data.result.result)

    const parsedResponse = dJSON.parse(myresult)
    console.log('parsedResponse: ' + parsedResponse)

    this.reviewlist = parsedResponse
    this.cardkey += 1
  }

  async function axiosGetProds () {
    console.log('thedata: ' + tchainid + ' ' + contractaddy + ' ' + myurl3)
    const axr = await this.axiosGetProducts(tchainid, contractaddy, myurl3)
    const axrsorted = axr.slice().sort()
    console.log('sorted: -- : ' + axrsorted)
    this.productlist = []
    this.productlist = Object.assign(axrsorted)
    console.log('new this.productlist: ' + axrsorted)
  }

  async function reloadProducts (wcat) {
    var i = 0
    while (i < 10) {
      i += 1
      await this.msleep(2000).then(() => {
        this.axiosGetProds()
      })
      if (this.productlist.indexOf(wcat) > -1) { // found it
        break
      }
    }
    // reset results form
    this.$refs.vselone.reset()
    this.showprodkey += 1
  }

  async function wreview () {
    this.writeresult = ' '
    this.writeresultkey += 1
    const wcat = this.vmcat
    const wrev = this.vmrev
    this.$refs.wform.reset()
    console.log('reset the form')
    console.log('wcat category being written to: ' + wcat)
    console.log('wrev review being written: ' + wrev)
    const axiosresp = await this.writeReview(wcat, wrev)
    if (typeof (axiosresp.data.result) === 'undefined') {
      var badanswerstr = 'Write Review Failed. Make sure both fields contain alpha-numeric values.'
      alert(badanswerstr)
    } else {
      this.productlist = ['Please wait', 'Blockchain is updating']
      this.showprodkey += 1
      console.log('wreview received response axiosresp: ' + axiosresp)
      const axiosrespstring = JSON.stringify(axiosresp)
      console.log('wreview received response myaxiosresp: ' + axiosrespstring)
      const partresult = JSON.stringify(axiosresp.data.result)
      const partb = JSON.stringify(axiosresp.status)
      const partc = JSON.stringify(axiosresp.statusText)
      this.writeresult = partresult + '\nStatus code: ' + partb + ' Status text: ' + partc
      this.writeresultkey += 1
      this.reloadProducts(wcat)
    }
  }

  function msleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time))
  }

  export default {
    name: 'AllReviews',
    data: () => ({
      showprodkey: 0,
      writeresultkey: 0,
      prodkey: 0,
      review: '',
      writeresult: '',
      vmcat: '',
      vmrev: '',
      productlist: [],
      prodchoice: '',
      reviewlist: '',
      chainid: tchainid,
      contracts: [contractaddy],
    }),

    computed: {
      styleContract () {
        return (window.outerWidth < 960) ? { fontSize: '11px' } : {}
      },
      styleTextareaSz () {
        return (window.outerWidth < 960) ? { width: '224px' } : { width: '424px' }
      },
      computedHeight () {
        return (window.outerWidth < 960) ? { height: '624px' } : { height: '424px' }
      },
      styleObjMaxWidth () {
        return (window.outerWidth < 960) ? { 'max-width': '290px' } : { 'max-width': '424px' }
      },
      yesbig () {
        return (window.outerWidth > 959)
      },
    },
    mounted () {
      this.axiosGetProds() // get the prod list
      if (window.outerWidth < 960) {
        this.$store.dispatch('gMobileAct', true)
        console.log('yes mobile')
        console.log(this.$vuetify.application.top)
      }
    },
    methods: {
      msleep,
      axiosGetRevs,
      axiosGetProducts,
      axiosGetProds,
      writeReview,
      wreview,
      reloadProducts,
    },
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=PT+Sans+Narrow&display=swap');

  .v-data-table__wrapper {
    font-size: small;
  }
  .ptsans {
    font-family:'PT Sans Narrow, sans-serif';
    font-weight: 400;
    font-size: 12px;
  }
  .v-label  {
    font-size: 12px!important;
    font-weight: 700;
    font-family: 'Raleway', sans-serif;
    color: black;
  }
  .tealback {
    background-image: linear-gradient(306deg, teal 70%, cyan 30% );
  }
  .montyfont {
    font-family: 'Montserrat',sans-serif;
    letter-spacing: 1.25px;
  }
  .textlow {
    text-transform: lowercase;
  }
</style>
