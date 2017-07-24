require "tweetstream"
require "faker"
require_relative "config"

def hashtag_list
  {
    got: " You belong to the #{Faker::GameOfThrones.house} house. Winter is here !! #got ",
    harrypotter: " You belong to the #{Faker::HarryPotter.house} house ! #HarryPotter"
  }
end

def available_hashtags
  hashtag_list.keys.map{|k|"##{k}"}.join(", ")
end

def send_regards(user)
  @rest_client.update("Hello @#{user} ! Try to use one of my availaible hashtags: #{available_hashtags} ")
end

def reply_to_user(user,message)
  @rest_client.update("Hi @#{user} ! #{message}")
  p "#{user} got an answer !"
end

def hashtag_symbols(hashtags)
  hashtags.map{|ht| ht.text.downcase.to_sym }
end

def process_hashtags(hashtags,user)
  hashtag_symbols(hashtags).each{ |ht|
    reply_to_user(user,hashtag_list[ht]) if hashtag_list[ht]
  }
end

def check_status(status)
  #Have any hashtag?
  return send_regards(status.user.screen_name) unless status.hashtags?

  process_hashtags(status.hashtags,status.user.screen_name)
end


@stream_client = TweetStream::Client.new(stream_config)

@rest_client = Twitter::REST::Client.new(rest_config)

@stream_client.on_timeline_status do |status|
  #If someone mentions the bot @sanatem_bot
  if status.user_mentions.any? { |mention| mention.screen_name == ENV["TWITTER_ACCOUNT"] }
    p "Mention from #{status.user.screen_name}"
    check_status(status)
  end

end

@stream_client.userstream
