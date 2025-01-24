import numpy as np
from numpy.polynomial import polynomial as poly

class QuantumSafeCipher:
    def __init__(self, n=256, q=12289):
        self.n = n  # Polynomial degree
        self.q = q  # Modulus
        
    def _random_tiny_poly(self):
        """Polynomial with small coefficients (-1, 0, 1)"""
        return np.random.randint(-1, 2, self.n, dtype=np.int64)
    
    def _random_error_poly(self):
        """Error polynomial with small coefficients"""
        return np.random.randint(-2, 3, self.n, dtype=np.int64)
    
    def generate_keys(self):
        """Generate public/private key pair"""
        while True:
            f = self._random_tiny_poly()
            try:
                f_inv = poly.Polynomial(poly.polyinv(f, self.q))
                break
            except:
                pass  # Retry if polynomial isn't invertible
                
        g = self._random_tiny_poly()
        h = poly.polymul(f_inv.coef, g) % self.q
        return h[:self.n].astype(np.int64), f
    
    def encrypt(self, pub_key, message):
        """Encrypt message with public key"""
        r = self._random_tiny_poly()
        e = self._random_error_poly()
        ciphertext = (poly.polymul(r, pub_key) + message + e) % self.q
        return ciphertext[:self.n].astype(np.int64)
    
    def decrypt(self, priv_key, ciphertext):
        """Decrypt ciphertext with private key"""
        temp = poly.polymul(ciphertext, priv_key) % self.q
        # Center lift to recover message
        return np.round(temp % self.q - (temp >= self.q//2) * self.q).astype(np.int64)

if __name__ == "__main__":
    
    # Example usage
    qsc = QuantumSafeCipher(n=32, q=1024)  # Small params for demo
    pub, priv = qsc.generate_keys()
    
    message = np.array([0, 1, 0, 1] + [0]*28)  # 32-dim message
    print("Original message:", message[:4])
    
    ciphertext = qsc.encrypt(pub, message)
    decrypted = qsc.decrypt(priv, ciphertext)
    print("Decrypted message:", decrypted[:4])
    