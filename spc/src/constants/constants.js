
var chainid = 4810
var passwd = 'kathy123'
var contaddy = 'SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC'
var sender = 'SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa'
var owner = 'SPEXdKRT4hTzACffQBAP8jUwtJsaTg36b4uH7d' // new aug10
var buyer = 'SPEXdKRT4nfcKKVqSt1XLdJYMp2H1nwy3oZ1nJ'

var valueasset = 2500000000
var gasprice = 90000
var gaslimit = 10000000

var url3 = 'https://westteam.nulstar.com:8003'
var url4 = 'https://westteam.nulstar.com:8004/jsonrpc'

const reqDataObj = {
  chainid,
  passwd,
  contaddy,
  sender,
  owner,
  buyer,
  valueasset,
  gasprice,
  gaslimit,
  url3,
  url4,
}

export default {
  name: 'reqDataObj',
  data: {
    reqDataObj,
  },
}
