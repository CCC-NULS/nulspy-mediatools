/* eslint-disable no-unused-vars */
// /eslint camelcase: [2, {properties: "never"}]/
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import cobj from '@/constants/constants.js'
import https from 'https'

var accStr = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
var restTypes = '"GET, POST, HEAD, UPDATE"'
// var AccessContExpHeadersRange = 'bytes=0-499'
var jsonversion = '2.0'

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

export async function axiosGetReviewsMain(chainid, contaddy, productId, url3) {
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const jsonversion = '2.0'
  const queryid = 900092
  const reqtype = 'getReviews'
  const vParams = [chainid, contaddy, reqtype, returntype, lastlist]
  const axiosi = makeaxio
  console.log('line32 ')

  try {
    var axresult
    console.log('inside axiosPost vParams: ' + vParams)
    axresult = await axiosi.post(url3, {
      jsonrpc: jsonversion,
      method: invokemethod,
      id: queryid,
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
  const invokemethod = 'invokeView'
  const reqtype = 'getAllProductIds'
  const returntype = '() return String'
  const lastlist = []
  const jsonversion = '2.0'
  const vParams = [chainid, contaddy, reqtype, returntype, lastlist]
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
      jsonrpc: jsonversion,
      method: invokemethod,
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
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const jsonversion = '2.0'
  const queryid = 900097

  const reqtype = 'getAccountContractList'
  const vparams = [this.chainid, this.contractaddy, reqtype, returntype, lastlist]
  const axiosi = makeaxio
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await axiosi.post(this.url3, {
      jsonrpc: jsonversion,
      method: invokemethod,
      id: queryid,
      params: vparams,
    })
  } catch (e) {
    console.log(e)
  }
  this.reviews = JSON.parse(axresult.data.result.result)
  console.log('this.reviews: ' + this.reviews)
  this.cardkey += 1
}
export async function writeReview(writeproduct, wreview) {
  const contract = cobj.data.cobj.contaddy
  const sender = cobj.data.cobj.sender
  const valueasset = cobj.data.cobj.valueasset // val * multiplier
  const gasprice = cobj.data.cobj.gasprice
  const gaslimit = cobj.data.cobj.gaslimit
  const args = [writeproduct, wreview]
  const contract_methodname = 'writeReview'
  const invokemethod = 'contractCall'
  const remark = 'call contract'
  const contractdesc = '(String productId, String reviewComments) return LReviewContract$Review;'

  const vparams = [cobj.data.cobj.chainid, sender, cobj.data.cobj.passwd, valueasset, gaslimit, gasprice,
    contract, contract_methodname, contractdesc, args, remark]

  const axiosi = makeaxio
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await axiosi.post(cobj.data.cobj.url4, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: 900099,
      params: vparams,
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
