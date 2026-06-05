from backend.pipeline.compiler import AppCompiler

compiler = AppCompiler()

result = compiler.compile(
    "Build a CRM with login, contacts, dashboard and premium payments. Admins can view analytics."
)

print(result)