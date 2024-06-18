import numpy as np

def U(x, data):
    # Hàm năng lượng tiềm năng (negative log-likelihood)
    return np.sum((x - data)**2) / 2

def grad_U(x, data):
    # Gradient của năng lượng tiềm năng
    return x - data

def control_variate_gradient(x, data, mean_grad):
    # Tính gradient với biến điều khiển
    return grad_U(x, data) - mean_grad

def cvg_hmc(U, grad_U, x0, data, n_samples=1000, step_size=0.01, n_steps=10, mass=1.0):
    samples = []
    x = x0
    m = mass
    eta = np.sqrt(2 * step_size)
    
    # Tính trung bình gradient ban đầu
    mean_grad = np.mean([grad_U(x0, data[i]) for i in range(len(data))], axis=0)
    
    for _ in range(n_samples):
        # Lấy mẫu động lượng từ phân phối chuẩn
        p = np.random.normal(0, np.sqrt(m))
        
        for _ in range(n_steps):
            idx = np.random.randint(len(data))
            grad = control_variate_gradient(x, data[idx], mean_grad)
            
            # Cập nhật động lượng
            p = p - step_size * grad + np.random.normal(0, eta)
            
            # Cập nhật vị trí
            x = x + step_size * p / m
        
        samples.append(x.copy())
    
    return np.array(samples)