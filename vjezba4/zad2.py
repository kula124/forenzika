from PIL import Image
import hashlib
putanja = "slika.png"
checksum_md5 = hashlib.md5(open(putanja, 'rb').read()).hexdigest()
checksum_sha1 = hashlib.sha1(open(putanja, 'rb').read()).hexdigest()
checksum_sha224 = hashlib.sha224(open(putanja,
                                      'rb').read()).hexdigest()
checksum_sha256 = hashlib.sha256(open(putanja,
                                      'rb').read()).hexdigest()
checksum_sha384 = hashlib.sha384(open(putanja,
                                      'rb').read()).hexdigest()
checksum_sha512 = hashlib.sha512(open(putanja,
                                      'rb').read()).hexdigest()
print("MD5 - " + checksum_md5)
print("SHA1 - " + checksum_sha1)
print("SHA224 - " + checksum_sha224)
print("SHA256 - " + checksum_sha256)
print("SHA384 - " + checksum_sha384)
print("SHA512 - " + checksum_sha512)

putanja_2 = "changedImage.png"
checksum_md5_2 = hashlib.md5(open(putanja_2, 'rb').read()).hexdigest()
checksum_sha1_2 = hashlib.sha1(open(putanja_2, 'rb').read()).hexdigest()
checksum_sha224_2 = hashlib.sha224(open(putanja_2,
                                        'rb').read()).hexdigest()
checksum_sha256_2 = hashlib.sha256(open(putanja_2,
                                        'rb').read()).hexdigest()
checksum_sha384_2 = hashlib.sha384(open(putanja_2,
                                        'rb').read()).hexdigest()
checksum_sha512_2 = hashlib.sha512(open(putanja_2,
                                        'rb').read()).hexdigest()

print("--------------Promjenjena slika--------------")
print("MD5 - " + checksum_md5_2)
print("SHA1 - " + checksum_sha1_2)
print("SHA224 - " + checksum_sha224_2)
print("SHA256 - " + checksum_sha256_2)
print("SHA384 - " + checksum_sha384_2)
print("SHA512 - " + checksum_sha512_2)
