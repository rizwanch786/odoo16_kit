from odoo import http
from odoo.http import request
from subprocess import Popen, PIPE


class GitHubWebhook(http.Controller):

    @http.route('/webhook-endpoint', type='http', auth='none', methods=['POST'], csrf=False)
    def handle_webhook(self, **post):
        # Replace 'your-secret-token' with your secret token
        secret_token = 'a36c62b04d6ffcb7dc8d628fee26e33694e8684c'

        # Get the GitHub signature from the headers
        signature = request.httprequest.headers.get('X-Hub-Signature')

        # Verify the signature
        if not self._verify_signature(request.httprequest.data, secret_token, signature):
            return http.Response('Invalid Signature', status=403)

        # Pull changes from the GitHub repository (implement this function)
        self._pull_changes()

        return http.Response('Webhook received successfully', status=200)

    def _verify_signature(self, payload, secret, signature):
        import hmac
        import hashlib

        # Check if the secret token is set
        if not secret or not signature:
            return False

        # Verify the signature
        sha_name, signature = signature.split('=')
        mac = hmac.new(secret.encode('utf-8'), msg=payload, digestmod=hashlib.sha1)
        return hmac.compare_digest(mac.hexdigest(), signature)

    def _pull_changes(self):
        # Replace 'your/repo' with your GitHub repository URL
        repo_url = 'https://github.com/rizwanch786/odoo16_kit.git'

        # Replace 'your-branch' with the branch you want to pull
        branch = 'main'

        # Path to your Odoo addons directory
        addons_path = '/opt/odoo16kit/odoo-custom-addons/odoo16_kit'

        # Pull changes using git
        cmd = ['git', 'pull', '--force', '--recurse-submodules', repo_url, branch]
        process = Popen(cmd, cwd=addons_path, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        # Log the result (you can customize this based on your needs)
        if process.returncode == 0:
            self._log_info(f'Successfully pulled changes from {repo_url}/{branch}')
        else:
            self._log_error(f'Error pulling changes: {stderr.decode("utf-8")}')

    def _log_info(self, message):
        # Replace this with your preferred logging mechanism
        print(f'INFO: {message}')

    def _log_error(self, message):
        # Replace this with your preferred logging mechanism
        print(f'ERROR: {message}')
