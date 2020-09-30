
var chainid = 4810
var passwd = 'kathy123'
var contaddy = 'SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC'
var sender = 'SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa'
var owner = 'SPEXdKRT4hTzACffQBAP8jUwtJsaTg36b4uH7d' // new aug10
var buyer = 'SPEXdKRT4nfcKKVqSt1XLdJYMp2H1nwy3oZ1nJ'

var valueasset = 2500000000
var gasprice = 90000
var gaslimit = 10000000

var url3 = 'http://westteam.nulstar.com:8003'
var url4 = 'http://westteam.nulstar.com:8004/jsonrpc'

const requestData = {
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
  name: 'rDataObj',
  data: {
    requestData,
  },
}
