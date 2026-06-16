import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp

class MAT499CalculusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MAT499 MULTIVARIABLE CALCULUS LAB ASSIGNMENT")
        self.root.geometry("720x520")
        self.root.resizable(False, False)
        
        
        style = ttk.Style()
        style.theme_use('clam')
        
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=12, pady=12)
        
        
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="Task 1: Techniques of Integration")
        self.notebook.add(self.tab2, text="Task 2: Multiple Integrals")
        
        self.build_task1_ui()
        self.build_task2_ui()
        
    def build_task1_ui(self):
        
        header_lbl = tk.Label(self.tab1, text="Techniques of Integration", font=("Arial", 14, "bold"), fg="blue")
        header_lbl.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=15)
        
        
        lbl_f1 = tk.Label(self.tab1, text="Enter function f(x):", font=("Arial", 11, "bold"))
        lbl_f1.grid(row=1, column=0, sticky="e", padx=20, pady=12)
        self.entry_f1 = ttk.Entry(self.tab1, width=45, font=("Consolas", 11))
        self.entry_f1.grid(row=1, column=1, sticky="w", padx=10, pady=12)
        self.entry_f1.insert(0, "x * log(x)")  # Standard placeholder example
        
        
        lbl_tech = tk.Label(self.tab1, text="Select technique:", font=("Arial", 11, "bold"))
        lbl_tech.grid(row=2, column=0, sticky="e", padx=20, pady=12)
        self.combo_tech = ttk.Combobox(self.tab1, width=42, font=("Arial", 11), state="readonly")
        self.combo_tech['values'] = ("Direct Integration", "Substitution", "Integration by Parts")
        self.combo_tech.current(2)  # Default to Integration by Parts
        self.combo_tech.grid(row=2, column=1, sticky="w", padx=10, pady=12)
        
        
        self.btn_integrate = ttk.Button(self.tab1, text="Integrate", command=self.run_task1_integration)
        self.btn_integrate.grid(row=3, column=0, columnspan=2, pady=20)
        
        
        lbl_res1 = tk.Label(self.tab1, text="Result:", font=("Arial", 11, "bold"))
        lbl_res1.grid(row=4, column=0, sticky="ne", padx=20, pady=10)
        
        self.txt_result1 = tk.Text(self.tab1, width=48, height=6, font=("Consolas", 12), relief="solid", bd=1, bg="white")
        self.txt_result1.grid(row=4, column=1, sticky="w", padx=10, pady=10)
        
    def build_task2_ui(self):
        
        header_lbl = tk.Label(self.tab2, text="Double Integral Calculator", font=("Arial", 14, "bold"), fg="blue")
        header_lbl.grid(row=0, column=0, columnspan=4, sticky="w", padx=20, pady=15)
        
        
        lbl_f2 = tk.Label(self.tab2, text="Enter f(x,y):", font=("Arial", 11, "bold"))
        lbl_f2.grid(row=1, column=0, sticky="e", padx=20, pady=12)
        self.entry_f2 = ttk.Entry(self.tab2, width=48, font=("Consolas", 11))
        self.entry_f2.grid(row=1, column=1, columnspan=3, sticky="w", padx=10, pady=12)
        self.entry_f2.insert(0, "x**2 * y")  
        
        
        lbl_a = tk.Label(self.tab2, text="Lower limit a (x):", font=("Arial", 10))
        lbl_a.grid(row=2, column=0, sticky="e", padx=20, pady=8)
        self.entry_a = ttk.Entry(self.tab2, width=14, font=("Consolas", 10))
        self.entry_a.grid(row=2, column=1, sticky="w", padx=10, pady=8)
        self.entry_a.insert(0, "0")
        
        lbl_b = tk.Label(self.tab2, text="Upper limit b (x):", font=("Arial", 10))
        lbl_b.grid(row=2, column=2, sticky="e", padx=20, pady=8)
        self.entry_b = ttk.Entry(self.tab2, width=14, font=("Consolas", 10))
        self.entry_b.grid(row=2, column=3, sticky="w", padx=10, pady=8)
        self.entry_b.insert(0, "2")
        
        
        lbl_c = tk.Label(self.tab2, text="Lower limit c (y):", font=("Arial", 10))
        lbl_c.grid(row=3, column=0, sticky="e", padx=20, pady=8)
        self.entry_c = ttk.Entry(self.tab2, width=14, font=("Consolas", 10))
        self.entry_c.grid(row=3, column=1, sticky="w", padx=10, pady=8)
        self.entry_c.insert(0, "1")
        
        lbl_d = tk.Label(self.tab2, text="Upper limit d (y):", font=("Arial", 10))
        lbl_d.grid(row=3, column=2, sticky="e", padx=20, pady=8)
        self.entry_d = ttk.Entry(self.tab2, width=14, font=("Consolas", 10))
        self.entry_d.grid(row=3, column=3, sticky="w", padx=10, pady=8)
        self.entry_d.insert(0, "3")
        
        
        self.btn_evaluate = ttk.Button(self.tab2, text="Evaluate", command=self.run_task2_evaluation)
        self.btn_evaluate.grid(row=4, column=0, columnspan=4, pady=20)
        
        
        lbl_res2 = tk.Label(self.tab2, text="Result:", font=("Arial", 11, "bold"))
        lbl_res2.grid(row=5, column=0, sticky="ne", padx=20, pady=10)
        
        self.txt_result2 = tk.Text(self.tab2, width=48, height=6, font=("Consolas", 12), relief="solid", bd=1, bg="white")
        self.txt_result2.grid(row=5, column=1, columnspan=3, sticky="w", padx=10, pady=10)
        
    def run_task1_integration(self):
        self.txt_result1.delete("1.0", tk.END)
        raw_expr = self.entry_f1.get().strip()
        technique = self.combo_tech.get()
        
        if not raw_expr:
            messagebox.showerror("Input Error", "Function field f(x) cannot be empty!")
            return
            
        try:
            x = sp.Symbol('x')
            parsed_expr = sp.sympify(raw_expr)
            computed_integral = sp.integrate(parsed_expr, x)
            
            
            formatted_output = f"Method Applied: {technique}\n"
            formatted_output += f"Analytical Solution Form:\n"
            formatted_output += f"= {computed_integral} + C\n\n"
            formatted_output += f"Formatted Typography:\n{sp.pretty(computed_integral)} + C"
            
            self.txt_result1.insert(tk.END, formatted_output)
        except Exception as err:
            messagebox.showerror("Mathematical Parsing Error", f"Invalid mathematical syntax inside f(x).\nDetails: {err}")

    def run_task2_evaluation(self):
        self.txt_result2.delete("1.0", tk.END)
        raw_expr = self.entry_f2.get().strip()
        val_a = self.entry_a.get().strip()
        val_b = self.entry_b.get().strip()
        val_c = self.entry_c.get().strip()
        val_d = self.entry_d.get().strip()
        
        if not all([raw_expr, val_a, val_b, val_c, val_d]):
            messagebox.showerror("Input Error", "All function and variable boundary parameters must be fulfilled!")
            return
            
        try:
            x, y = sp.symbols('x y')
            parsed_expr = sp.sympify(raw_expr)
            
            
            lim_a = sp.sympify(val_a)
            lim_b = sp.sympify(val_b)
            lim_c = sp.sympify(val_c)
            lim_d = sp.sympify(val_d)
            
            
            computed_double = sp.integrate(parsed_expr, (y, lim_c, lim_d), (x, lim_a, lim_b))
            
            formatted_output = f"Evaluation Order: ∫[a to b] ∫[c to d] f(x,y) dy dx\n"
            formatted_output += f"Exact Symbolic Value:\n"
            formatted_output += f"= {computed_double}\n\n"
            formatted_output += f"Formatted Typography:\n{sp.pretty(computed_double)}"
            
            self.txt_result2.insert(tk.END, formatted_output)
        except Exception as err:
            messagebox.showerror("Mathematical Parsing Error", f"Unable to evaluate. Verify functions and integration boundaries.\nDetails: {err}")

if __name__ == "__main__":
    window = tk.Tk()
    app = MAT499CalculusGUI(window)
    window.mainloop()