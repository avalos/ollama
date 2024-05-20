import os
import asyncio

# Set LD_LIBRARY_PATH so the system NVIDIA library
#os.environ.update({'LD_LIBRARY_PATH': '/usr/lib64-nvidia'})

async def run_process(cmd):
    print('>>> starting', *cmd)
    p = await asyncio.subprocess.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    async def pipe(lines):
        async for line in lines:
            print(line.strip().decode('utf-8'))

    await asyncio.gather(
        pipe(p.stdout),
        pipe(p.stderr),
    )

async def main():
    ngrok_token = os.getenv('NGROK_AUTHTOKEN')
    port = os.getenv('PORT')

    if not ngrok_token:
        raise ValueError("NGROK_AUTHTOKEN environment variable not set")
    if not port:
        raise ValueError("PORT environment variable not set")

    await asyncio.gather(
        run_process(['ngrok', 'config', 'add-authtoken', ngrok_token])
    )

    await asyncio.gather(
        run_process(['ngrok', 'http', '--log', 'stderr', port, '--host-header', f'localhost:{port}'])
    )

if __name__ == "__main__":
    asyncio.run(main())
