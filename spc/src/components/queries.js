/* eslint-disable dot-notation */
/* eslint-disable no-unused-vars */
// /eslint camelcase: [2, {properties: "never"}]/
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import rDataObj from '@/constants/dataConstants.js'
import https from 'https'

var accStr = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
var restTypes = '"GET, POST, HEAD, OPTIONS"'
// var Access-Control-Expose-Headers-Range = 'bytes=0-499'
var jsonversion = '2.0'

function mymakeaxio() {
  const locAxiosConfig = axios.create({
    httpsAgent: new https.Agent({ keepAlive: true }),
    defaults: {
      headers: {
        common: {
          Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Content-Type': 'application/json;charset=utf-8',
          'Access-Control-Allow-Origin': '*',
        },
        post: {
          Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Content-Type': 'application/json;charset=utf-8',
          'Access-Control-Allow-Origin': '*',
        },
      },
    },
  })
  return locAxiosConfig
}

export async function axiosGetReviewsMain(chainid, contaddy, productId, url3) {
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const jsonversion = '2.0'
  const queryid = 900092
  const reqtype = 'getReviews'
  const vParams = [chainid, contaddy, reqtype, returntype, lastlist]
  const madeaxiosGetRevs = mymakeaxio()
  console.log('line32 ')

  try {
    var axresult
    console.log('inside axiosPost vParams: ' + vParams)
    axresult = await madeaxiosGetRevs.post(url3, {
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
  console.log('here now in queries axiosGetProducts')
  const invokemethod = 'invokeView'
  const reqtype = 'getAllProductIds'
  const returntype = '() return String'
  const lastlist = []
  const jsonversion = '2.0'
  const vParams = [chainid, contaddy, reqtype, returntype, lastlist]
  const madeaxiosGetProds = mymakeaxio()
  console.log('inside axiosGetProducts')
  var mystr = Object.getOwnPropertyNames(madeaxiosGetProds)
  console.log(mystr)
  console.log(Object.values(madeaxiosGetProds))
  console.log('inside axiosGetProducts accStr & vParams: ' + accStr + ' - ' + vParams)
  console.log('inside axiosGetProducts defaults: ' + madeaxiosGetProds.defaults)
  console.log('sending a post: ' + madeaxiosGetProds.defaults + ' - ' + madeaxiosGetProds.headers)
  var axresult

  try {
    axresult = await madeaxiosGetProds.post(u3, {
      jsonrpc: jsonversion,
      method: invokemethod,
      id: 900099,
      params: vParams,
    })
  } catch (e) {
    console.log(e)
  }
  var thisproducts
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
  const madeaxiosGetContracts = mymakeaxio()
  console.log('just made new axios object in axiosGetContracts')
  console.log('here is some info')
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await madeaxiosGetContracts.post(this.url3, {
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
  const contract = rDataObj.data.requestDatacontaddy
  const sender = rDataObj.data.requestDatasender
  const valueasset = rDataObj.data.requestDatavalueasset // val * multiplier
  const gasprice = rDataObj.data.requestDatagasprice
  const gaslimit = rDataObj.data.requestDatagaslimit
  const args = [writeproduct, wreview]
  const contract_methodname = 'writeReview'
  const invokemethod = 'contractCall'
  const remark = 'call contract'
  const contractdesc = '(String productId, String reviewComments) return LReviewContract$Review;'

  const vparams = [rDataObj.data.requestDatachainid, sender, rDataObj.data.requestDatapasswd, valueasset, gaslimit, gasprice,
    contract, contract_methodname, contractdesc, args, remark]

  const madeaxiosWriteReview = mymakeaxio()
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await madeaxiosWriteReview.post(rDataObj.data.requestDataurl4, {
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
    mymakeaxio,
  },
}
