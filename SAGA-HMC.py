import numpy as np

def U(x, data):
    # Hàm năng lượng tiềm năng (negative log-likelihood)
    return np.sum((x - data)**2) / 2

def grad_U(x, data):
    # Gradient của năng lượng tiềm năng
    return x - data

def saga_hmc(U, grad_U, x0, data, n_samples=1000, step_size=0.01, n_steps=10, mass=1.0):
    samples = []
    x = x0
    m = mass
    eta = np.sqrt(2 * step_size)
    
    n_data = len(data)
    gradient_memory = np.zeros((n_data, len(x0)))
    gradient_avg = np.zeros(len(x0))
    
    for i in range(n_data):
        gradient_memory[i] = grad_U(x0, data[i])
    
    gradient_avg = np.mean(gradient_memory, axis=0)
    
    for _ in range(n_samples):
        # Lấy mẫu động lượng từ phân phối chuẩn
        p = np.random.normal(0, np.sqrt(m))
        
        for _ in range(n_steps):
            idx = np.random.randint(n_data)
            grad = grad_U(x, data[idx])
            old_grad = gradient_memory[idx]
            gradient_memory[idx] = grad
            gradient_avg += (grad - old_grad) / n_data
            
            # Cập nhật động lượng
            p = p - step_size * (grad - old_grad + gradient_avg) + np.random.normal(0, eta)
            
            # Cập nhật vị trí
            x = x + step_size * p / m
        
        samples.append(x.copy())
    
    return np.array(samples)