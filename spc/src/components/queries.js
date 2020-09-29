/* eslint-disable dot-notation */
/* eslint-disable no-unused-vars */
// /eslint camelcase: [2, {properties: "never"}]/
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */
// axios.get(url, { httpsAgent }) // // or // const instance = axios.create({ myhttpsAgent })

// responseType = json
// withCredentials: true,

import axios from 'axios'
import rDataObj from '@/constants/dataConstants.js'
import https from 'https'
const fsx = require('fs-extra')


var myhttpsAgent = new https.Agent({
  cert: fsx.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem'),
  key: fsx.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem'),
})

const postOrGetHeader = {
  Host: 'westteam.nulstar.com',
  Origin: 'https://westteam.nulstar.com',
  'Content-Type': 'application/json',
}

const postOptHeader = {
  Host: 'westteam.nulstar.com',
  Origin: 'https://westteam.nulstar.com',
  'Access-Control-Request-Method': 'POST',
  'Access-Control-Request-Headers': 'Authorization, Content-Type',
}

const myconfig = axios.create({
  myhttpsAgent,
  defaults: {
    headers: {
      options: postOptHeader,
      post: postOrGetHeader,
      get: postOrGetHeader,
    },
  },
})

export async function axiosGetReviewsMain(chainid, contaddy, productId, url3) {
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const queryid = 900092
  const reqtype = 'getReviews'
  const getReviewsParams = [chainid, contaddy, reqtype, returntype, lastlist]
  const madeaxiosGetRevs = myconfig()
  console.log('inside axiosGetReviewsMain')

  try {
    var axresult
    axresult = await madeaxiosGetRevs.post(url3, {
      method: invokemethod,
      id: queryid,
      params: getReviewsParams,
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
  const getProdsParams = [chainid, contaddy, reqtype, returntype, lastlist]
  const getProdConf = myconfig()
  axios.interceptors.request.use(getProdConf => {
    console.log(getProdConf)
    return getProdConf
  })
  console.log('inside axiosGetProducts' + getProdConf.defaults + ' - ' + getProdConf.headers)

  try {
    var axresult
    console.log('axiosGetContracts getProdsParams: ' + getProdsParams)
    axresult = await getProdConf.post(this.url3, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: 99099,
      params: getProdsParams,
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
  const queryid = 900097

  const reqtype = 'getAccountContractList'
  const vparams = [this.chainid, this.contractaddy, reqtype, returntype, lastlist]
  const madeaxiosGetContracts = myconfig()
  console.log('just made new axios object in axiosGetContracts')
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await madeaxiosGetContracts.post(this.url3, {
      jsonrpc: '2.0',
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
  console.log('axiosGetContracts vparams: ' + vparams)

  const madeaxiosWriteReview = myconfig()
  try {
    var axresult
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
    myconfig,
  },
}
