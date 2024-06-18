import numpy as np

def U(x, data):
    # Hàm năng lượng tiềm năng (negative log-likelihood)
    return np.sum((x - data)**2) / 2

def grad_U(x, data):
    # Gradient của năng lượng tiềm năng
    return x - data

def SG_HMC(U, grad_U, x0, data, n_samples=1000, step_size=0.01, n_steps=10, mass=1.0):
    samples = []
    x = x0
    m = mass
    eta = np.sqrt(2 * step_size)
    
    for _ in range(n_samples):
        # Lấy mẫu động lượng từ phân phối chuẩn
        p = np.random.normal(0, np.sqrt(m))
        
        # Cập nhật động lượng với gradient của U
        p = p - step_size / 2 * grad_U(x, data) + np.random.normal(0, eta)
        
        for _ in range(n_steps):
            # Cập nhật vị trí
            x = x + step_size * p / m
            
            if _ != n_steps - 1:
                # Cập nhật động lượng trừ bước cuối cùng
                p = p - step_size * grad_U(x, data) + np.random.normal(0, eta)
        
        # Cập nhật động lượng một lần nữa
        p = p - step_size / 2 * grad_U(x, data) + np.random.normal(0, eta)
        
        samples.append(x.copy())
    
    return np.array(samples)

if __name__ == '__main__':

    # Ví dụ sử dụng SG-HMC để lấy mẫu từ phân phối Gaussian đơn giản
    data = np.array([5.0])  # dữ liệu ví dụ
    x0 = np.array([0.0])  # khởi tạo x ban đầu
    samples = SG_HMC(U, grad_U, x0, data, n_samples=1000, step_size=0.01, n_steps=10)

    # In ra một vài mẫu
    print(samples[:10])