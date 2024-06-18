import numpy as np

def U(x, data):
    # Hàm năng lượng tiềm năng (negative log-likelihood)
    return np.sum((x - data)**2) / 2

def grad_U(x, data):
    # Gradient của năng lượng tiềm năng
    return x - data

def full_gradient(U, grad_U, x, data):
    # Tính gradient đầy đủ trên toàn bộ dữ liệu
    return grad_U(x, data)

def svrg_hmc(U, grad_U, x0, data, n_samples=1000, step_size=0.01, n_steps=10, mass=1.0, m=5, n=10):
    samples = []
    x = x0
    m_grad = full_gradient(U, grad_U, x, data)
    m = mass
    eta = np.sqrt(2 * step_size)

    for _ in range(n_samples):
        p = np.random.normal(0, np.sqrt(m))
        p = p - step_size / 2 * (grad_U(x, data) - m_grad + full_gradient(U, grad_U, x, data)) + np.random.normal(0, eta)

        for _ in range(n_steps):
            x = x + step_size * p / m

            if _ % m == 0:
                m_grad = full_gradient(U, grad_U, x, data)
            
            if _ != n_steps - 1:
                p = p - step_size * (grad_U(x, data) - m_grad + full_gradient(U, grad_U, x, data)) + np.random.normal(0, eta)
        
        p = p - step_size / 2 * (grad_U(x, data) - m_grad + full_gradient(U, grad_U, x, data)) + np.random.normal(0, eta)
        samples.append(x.copy())

    return np.array(samples)