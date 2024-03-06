import CryptoES from 'crypto-es'

const keyStr = import.meta.env.VITE_AES_KEY
// 加密
export function encrypt(word) {
  const key = CryptoES.enc.Utf8.parse(keyStr)
  const srcs = CryptoES.enc.Utf8.parse(word)
  const encrypted = CryptoES.AES.encrypt(srcs, key, { mode: CryptoES.mode.ECB, padding: CryptoES.pad.Pkcs7 })
  return encrypted.toString()
}

// function decrypt(word) {
//   const key = CryptoES.enc.Utf8.parse(keyStr)
//   const decryptStr = CryptoES.AES.decrypt(word, key, { mode: CryptoES.mode.ECB, padding: CryptoES.pad.Pkcs7 })
//   return CryptoES.enc.Utf8.stringify(decryptStr).toString()
// }

export default { encrypt }
