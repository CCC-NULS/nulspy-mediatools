/* eslint-disable no-unused-vars */
// /eslint camelcase: [2, {properties: "never"}]/
/* eslint camelcase: ["warn", {allow: ["value_asset", "gas_limit", "gas_price", "contract_methodname", "contract_desc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import cobj from '@/constants/constants.js'
import https from 'https'

var accStr = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
var restTypes = '"GET, POST, HEAD, UPDATE"'
// var AccessContExpHeadersRange = 'bytes=0-499'
var jsonV = '2.0'

function makeaxio() {
  var rangelist = 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range'
  const axio = axios.create({
    defaults: {
      httpsAgent: new https.Agent({ keepAlive: true }),
      headers: {
        post: {
          Accept: accStr,
          'Access-Control-Allow-Methods': restTypes,
          'Content-Type': 'text/plain; charset=utf-8',
          'Access-Control-Allow-Headers': rangelist,
        },
      },
    },
  })
  return axio
}

export async function axiosGetReviewsMain(chainid, contaddy, productId, Url3) {
  const invMethod = 'invokeView'
  const RETtype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const jsonV = '2.0'
  const queryId = 900092
  const REQtype = 'getReviews'
  const vParams = [chainid, contaddy, REQtype, RETtype, lastlist]
  const axiosi = makeaxio
  console.log('line32 ')

  try {
    var axresult
    console.log('inside axiosPost vParams: ' + vParams)
    axresult = await axiosi.post(Url3, {
      jsonrpc: jsonV,
      method: invMethod,
      id: queryId,
      params: vParams,
    })
  } catch (e) {
    console.log(e)
  }
  console.log('axresult returning: ' + axresult)
  return axresult
}

export async function axiosGetProducts(chainid, contaddy, u3) {
  console.log('here now')
  const invMethod = 'invokeView'
  const REQtype = 'getAllProductIds'
  const RETtype = '() return String'
  const lastlist = []
  const jsonV = '2.0'
  const vParams = [chainid, contaddy, REQtype, RETtype, lastlist]
  var axresult
  var thisproducts
  var rangelist = 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range'
  const axio = axios.create(
    {
      defaults: {
        headers: {
          Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Content-Type': 'text/plain; charset=utf-8',
          'Access-Control': '*',
          'Access-Control-Expose-Headers': '*, Authorization',
          'Access-Control-Allow-Headers': rangelist,
        },
        httpsAgent: new https.Agent({ keepAlive: true }),
        post: {
          Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Access-Control-Allow-Methods': restTypes,
          'Content-Type': 'text/plain; charset=utf-8',
          'Access-Control-Expose-Headers': '*, Authorization',
          'Access-Control-Allow-Headers': rangelist,
        },
      },
    },
  )
  console.log('inside axiosGetProducts accStr & vParams: ' + accStr + ' - ' + vParams)

  try {
    axresult = await axio.post(u3, {
      jsonrpc: jsonV,
      method: invMethod,
      id: 900099,
      params: vParams,
    })
  } catch (e) {
    console.log(e)
  }
  thisproducts = JSON.parse(axresult.data.result.result)
  console.log('thisproducts: ' + thisproducts)
  // this.cardkey += 1;
  return thisproducts
}

async function axiosGetContracts() {
  var productId = this.prodchoice
  const invMethod = 'invokeView'
  const RETtype = '(String productId) return Ljava/util/List;'
  const LASTLIST = [productId]
  const jsonV = '2.0'
  const queryId = 900097

  const REQtype = 'getAccountContractList'
  const vPARAMS = [this.chainid, this.contractaddy, REQtype, RETtype, LASTLIST]
  const axiosi = makeaxio
  try {
    var axresult
    console.log('axiosGetContracts vPARAMS: ' + vPARAMS)
    axresult = await axiosi.post(this.Url3, {
      jsonrpc: jsonV,
      method: invMethod,
      id: queryId,
      params: vPARAMS,
    })
  } catch (e) {
    console.log(e)
  }
  this.reviews = JSON.parse(axresult.data.result.result)
  console.log('this.reviews: ' + this.reviews)
  this.cardkey += 1
}
export async function writeReview(wprod, wreview) {
  const contract = cobj.data.cobj.contaddy
  const sender = cobj.data.cobj.SENDER
  const value_asset = cobj.data.cobj.VALUE_ASSET // val * multiplier
  const gas_price = cobj.data.cobj.GAS_PRICE
  const gas_limit = cobj.data.cobj.GAS_LIMIT
  const args = [wprod, wreview]
  const contract_methodname = 'writeReview'
  const invMethod = 'contractCall'
  const remark = 'call contract'
  const contract_desc = '(String productId, String reviewComments) return LReviewContract$Review;'

  const vPARAMS = [cobj.data.cobj.chainid, sender, cobj.data.cobj.PW, value_asset, gas_limit, gas_price,
    contract, contract_methodname, contract_desc, args, remark]

  const axiosi = makeaxio
  try {
    var axresult
    console.log('axiosGetContracts vPARAMS: ' + vPARAMS)
    axresult = await axiosi.post(cobj.data.cobj.Url4, {
      jsonrpc: '2.0',
      method: invMethod,
      id: 900099,
      params: vPARAMS,
    })
  } catch (e) { console.log(e) }
  return axresult
}

export const MyQueries = {
  axiosGetContracts,
}

export default {
  methods: {
    makeaxio,
  },
}
