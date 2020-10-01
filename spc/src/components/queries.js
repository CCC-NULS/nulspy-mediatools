/* eslint-disable dot-notation */
/* eslint-disable no-unused-vars */
/* eslint camelcase: ["warn", {allow: ["valueasset", "gaslimit", "gasprice", "contract_methodname", "contractdesc" ]}] */
/* eslint space-before-function-paren: 0 */

import axios from 'axios'
import { cobj } from '@/constants/dataConstants.js'
import https from 'https'
const chainid = cobj.chainid
const contaddy = cobj.contaddy
const myurl3 = cobj.url3
const url4 = cobj.url4

const hsAgent = new https.Agent({ 
  ca: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem'),
  key: fs.readFileSync('/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem'),
});

function makeaxio() {
  const axioConfObj = axios.create({
    agent: hsAgent,
    jsonrpc: '2.0',
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
  return axioConfObj
}

export async function axiosGetReviewsMain(chainid, contaddy, productId, url3) {
  const returntype = '(String productId) return Ljava/util/List;'
  const lastlistw = [productId]
  const reqtype = 'getReviews'
  const getReviewsParams = [chainid, contaddy, reqtype, returntype, lastlistw]
  console.log('inside queries.axiosGetReviewsMain')
  console.log('c: ' + chainid + ' contaddy: ' + contaddy + ' reqtype: ' + reqtype + ' prodId: ' + productId)
  const axioObj = makeaxio()
  try {
    var axresultg
    axresultg = await axioObj.post(url3, {
      method: 'invokeView',
      id: '900092',
      'Content-Type': 'application/json;charset=UTF-8',
      params: getReviewsParams,
    })
  } catch (e) {
    console.log(e)
  }
  console.log('done in queries.axiosGetReviewsMain')
  console.log('axresultg.data.result.result: ' + axresultg.data.result.result)
  console.log('axresultg returning: ' + axresultg)
  return axresultg
}

export async function axiosGetProducts(chainid, contaddy, url3) {
  console.log('here now in queries axiosGetProducts')
  const reqtype = 'getAllProductIds'
  const returntype = '() return String'
  const lastlist = []
  const getProdsParams = [chainid, contaddy, reqtype, returntype, lastlist]
  axios.interceptors.request.use(localconf => {
    console.log(localconf)
    return localconf
  })
  const axioGetProds = makeaxio()

  try {
    var axresult
    console.log('axiosGetContracts getProdsParams: ' + getProdsParams)
    axresult = await axioGetProds.post(url3, {
      method: 'invokeView',
      id: 99099,
      params: getProdsParams,
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
  const lastlistp = [productId]
  const queryid = 900097

  const reqtype = 'getAccountContractList'
  const vparams = [this.chainid, this.contractaddy, reqtype, returntype, lastlistp]
  console.log('just made new axios object in axiosGetContracts')
  const axioGetContr = makeaxio()

  try {
    var axresult
    console.log('axiosGetContracts vparams: ' + vparams)
    axresult = await axioGetContr.post(myurl3, {
      method: invokemethod,
      id: queryid,
      params: vparams,
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
  const passwd = cobj.passwd
  const sender = cobj.sender
  const valueasset = cobj.valueasset
  const gasprice = cobj.gasprice
  const gaslimit = cobj.gaslimit

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
      method: invokemethod,
      id: 900099,
      params: vparams,
    })
  } catch (e) { console.log(e) }
  return axResWrite
}

export const MyQueries = {
  axiosGetContracts,
}
