
var chainid = 4810
var PW = 'kathy123'
// SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC   new contract august 10
var contaddy = 'SPEXdKRT4zmkrCMcwQKfWEQfmCCKSboHp4TCdC'
var SENDER = 'SPEXdKRT4pz7ZhasM9pTK4fvGrJf8eod5ZqtXa'
var OWNER = 'SPEXdKRT4hTzACffQBAP8jUwtJsaTg36b4uH7d' // new aug10
var BUYER = 'SPEXdKRT4nfcKKVqSt1XLdJYMp2H1nwy3oZ1nJ'

var VALUE_ASSET = 2500000000
var GAS_PRICE = 90000
var GAS_LIMIT = 10000000

var Url3 = 'https://westteam.nulstar.com:8003'
var Url4 = 'https://westteam.nulstar.com:8004/jsonrpc'

const cobj = {
  chainid,
  PW,
  contaddy,
  SENDER,
  OWNER,
  BUYER,
  VALUE_ASSET,
  GAS_PRICE,
  GAS_LIMIT,
  Url3,
  Url4,
}

export default {
  name: 'constants',
  data: {
    cobj,
  },
}
