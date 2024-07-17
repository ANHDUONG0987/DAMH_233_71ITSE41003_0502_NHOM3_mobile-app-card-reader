// Giả định một lớp Card để quản lý thông tin thẻ
class Card {
    String cardNumber;
    String cardHolderName;
    String expiryDate;

    // Constructor
    public Card(String cardNumber, String cardHolderName, String expiryDate) {
        this.cardNumber = cardNumber;
        this.cardHolderName = cardHolderName;
        this.expiryDate = expiryDate;
    }
}

// Giả định một lớp CardManager để quản lý danh sách thẻ
class CardManager {
    List<Card> cardList = new ArrayList<>();

    // Thêm thẻ vào danh sách
    public void addCard(Card card) {
        cardList.add(card);
    }

    // Xóa thẻ khỏi danh sách
    public void removeCard(Card card) {
        cardList.remove(card);
    }

    // Lấy danh sách thẻ
    public List<Card> getCardList() {
        return cardList;
    }
}

// Mẫu kiểm thử
public class CardManagerTest {
    public static void main(String[] args) {
        CardManager cardManager = new CardManager();

        // Thêm thẻ vào danh sách
        Card card1 = new Card("1234 5678 9012 3456", "John Doe", "12/24");
        Card card2 = new Card("9876 5432 1098 7654", "Jane Smith", "11/23");
        cardManager.addCard(card1);
        cardManager.addCard(card2);

        // Kiểm tra xem thẻ có trong danh sách hay không
        assert cardManager.getCardList().contains(card1);
        assert cardManager.getCardList().contains(card2);

        // Xóa thẻ khỏi danh sách
        cardManager.removeCard(card1);

        // Kiểm tra xem thẻ đã bị xóa hay chưa
        assert !cardManager.getCardList().contains(card1);
    }
}
