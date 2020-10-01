/* eslint-disable dot-notation */
/* eslint-disable no-unused-vars */
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import rDataObj from '@/constants/dataConstants.js'

function makeaxio() {
  const axioConfQbj = axios.create({
  defaults: {
    headers: {
      post: { 
        Accept: 'application/json, text/plain, text/html',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 
        'Content-Type': 'application/json;charset=UTF-8',
      },
      get: { 
        Accept: 'application/json, text/plain, text/html', 
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 
        'Content-Type': 'application/json;charset=UTF-8',
      },
      },
    },
  });
  return axioConfQbj
}

export async function axiosGetReviewsMain(chainid, contaddy, productId, url3) {
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const reqtype = 'getReviews'
  const getReviewsParams = [chainid, contaddy, reqtype, returntype, lastlist]
  console.log('inside queries.axiosGetReviewsMain')
  console.log('chainid: ' + chainid + ' chainid: ' + contaddy + ' reqtype: ' + reqtype + ' productId: ' + productId)
  const axioObj = makeaxio()
  try {
    var axresultg
    axresultg = await axioObj.post(url3, {
      method: 'invokeView',
      id: '900092',
      jsonrpc: '2.0',
      'Content-Type': 'application/json;charset=UTF-8',
      params: getReviewsParams,
    })
  } catch (e) {
    console.log(e)
  }
  console.log('done in queries.axiosGetReviewsMain')
  // console.log('axresultg.data: ' + axresultg.data)
  // console.log('axresultg.data.result: ' + axresultg.data.result)
  console.log('axresultg.data.result.result: ' + axresultg.data.result.result)
  console.log('axresultg returning: ' + axresultg)
  return axresultg
}

export async function axiosGetProducts(chainid, contaddy, url3) {
  console.log('here now in queries axiosGetProducts')
  const invokemethod = 'invokeView'
  const reqtype = 'getAllProductIds'
  const returntype = '() return String'
  const lastlist = []
  const getProdsParams = [chainid, contaddy, reqtype, returntype, lastlist]
  axios.interceptors.request.use( localconf => {
    console.log(localconf)
    return localconf
  })

  try {
    var axresult
    console.log('axiosGetContracts getProdsParams: ' + getProdsParams)
    axresult = await axios.post(url3, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: 99099,
      params: getProdsParams,
      headers: {
        'Content-Type': 'application/json',
      },
    })
  } catch (e) {
    console.log(e)
  }
  var thisproducts
  thisproducts = JSON.parse(axresult.data.result.result)
  console.log('done in axiosGetProducts. thisproducts: ' + thisproducts)
  // this.cardkey += 1;
  return thisproducts
}

async function axiosGetContracts() {
  var productId = this.prodchoice
  const invokemethod = 'invokeView'
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlist = [productId]
  const queryid = 900097
  const myurl3 = 'http://westteam.nulstar.com:8003'

  const reqtype = 'getAccountContractList'
  const vparams = [this.chainid, this.contractaddy, reqtype, returntype, lastlist]
  console.log('just made new axios object in axiosGetContracts')
  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await axios.post(myurl3, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: queryid,
      params: vparams,
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
      },
    })
  } catch (e) {
    console.log(e)
  }
  console.log('done in axiosGetContracts')

  this.reviews = JSON.parse(axresult.data.result.result)
  console.log('this.reviews: ' + this.reviews)
  this.cardkey += 1
}

export async function writeReview(writeproduct, wreview) {
  const dObj = this.rDataObj
  const chainid = dObj.data.tData.chainid
  const sender = dObj.data.tData.sender
  const passwd = dObj.data.tData.passwd

  const valueasset = dObj.data.tData.valueasset // val * multiplier
  const gaslimit = dObj.data.tData.gaslimit
  const gasprice = dObj.data.tData.gasprice
  const contract = dObj.data.tData.contaddy
  const args = [writeproduct, wreview]
  const contract_methodname = 'writeReview'
  const invokemethod = 'contractCall'
  const remark = 'call contract'
  const contractdesc = '(String productId, String reviewComments) return LReviewContract$Review;'

  const vparams = [chainid, sender, passwd, valueasset, gaslimit, gasprice,
    contract, contract_methodname, contractdesc, args, remark]
  console.log('axiosGetContracts vparams: ' + vparams)
  axios.interceptors.request.use( localconf => {
    console.log(localconf)
    return localconf
  })

  try {
    var axresult
    const myurl4 = dObj.data.tData.url4
    axresult = await axios.post(myurl4, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: 900099,
      params: vparams,
      headers: {
        Accept: 'application/json, text/plain, text/html',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 
        'Content-Type': 'application/json;charset=UTF-8',
      },
    })
  } catch (e) { console.log(e) }
  return axresult
}

export const MyQueries = {
  axiosGetContracts,
}
