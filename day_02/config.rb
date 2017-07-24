require_relative "env"

def stream_config
  {
    consumer_key:        ENV["CONSUMER_KEY"],
    consumer_secret:     ENV["CONSUMER_SECRET"],
    oauth_token:         ENV["ACCESS_TOKEN"],
    oauth_token_secret:  ENV["ACCESS_TOKEN_SECRET"],
    auth_method:         :oauth
  }
end

def rest_config
  {
    consumer_key:         ENV["CONSUMER_KEY"],
    consumer_secret:      ENV["CONSUMER_SECRET"],
    access_token:         ENV["ACCESS_TOKEN"],
    access_token_secret:  ENV["ACCESS_TOKEN_SECRET"],
  }
end
