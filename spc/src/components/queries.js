/* eslint-disable dot-notation */
/* eslint-disable no-unused-vars */
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import { cobj } from '@/constants/dataConstants.js'
const tchainid = cobj.chainid
const contractaddy = cobj.contaddy
const myurl3 = cobj.url3

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
  })
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
  axios.interceptors.request.use(localconf => {
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
  const chainid = cobj.chainid
  const passwd = cobj.passwd
  const contaddy = cobj.contaddy
  const sender = cobj.sender
  const owner = cobj.owner // new aug10
  const valueasset = cobj.valueasset
  const gasprice = cobj.gasprice
  const gaslimit = cobj.gaslimit
  const url4 = cobj.url4

  const args = [writeproduct, wreview]
  const contract_methodname = 'writeReview'
  const invokemethod = 'contractCall'
  const remark = 'call contract'
  const contractdesc = '(String productId, String reviewComments) return LReviewContract$Review;'
  console.log('gaslimit: ' + gaslimit)
  console.log('valueasset: ' + valueasset)
  console.log('sender: ' + sender)

  const vparams = [chainid, sender, passwd, valueasset, gaslimit, gasprice,
    contaddy, contract_methodname, contractdesc, args, remark]
  console.log('axiosGetContracts vparams: ' + vparams)
  console.log('axios.interceptors: ')
  const axioObjWrite = makeaxio()

  axios.interceptors.request.use(axioObjWrite => {
    console.log(axioObjWrite)
    return axioObjWrite
  })

  try {
    var axResWrite
    axResWrite = await axioObjWrite.post(url4, {
      jsonrpc: '2.0',
      method: invokemethod,
      id: 900099,
      params: vparams,
      'Content-Type': 'application/json;charset=UTF-8',
    })
  } catch (e) { console.log(e) }
  return axResWrite
}

export const MyQueries = {
  axiosGetContracts,
}
