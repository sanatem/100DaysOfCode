require "twitter"
require "tweetstream"
#require "faker"
require_relative "config"

@stream_client = TweetStream::Client.new(stream_config)

@rest_client = Twitter::REST::Client.new(rest_config)


@stream_client.on_timeline_status do |status|

  #If someone mentions the bot @sanatem_bot
  if status.user_mentions.any? { |mention| mention.screen_name == "sanatem_bot" }
    p "Mention from #{status.user.screen_name}"
    @rest_client.update("Hello nice to meet you ! @#{status.user.screen_name}")
  end

end

@stream_client.userstream
